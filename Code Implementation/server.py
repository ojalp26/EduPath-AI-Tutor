import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from google.genai import types
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools.tool_context import ToolContext

load_dotenv()
app = FastAPI()

# 1.5-flash is stable for logic
MODEL_NAME = "gemini-2.5-flash"
retry_config = types.HttpRetryOptions(attempts=5, exp_base=7, initial_delay=1, http_status_codes=[429, 500, 503, 504])

# --- TOOLS ---
def set_learning_goal(tool_context: ToolContext, level: str, topic: str) -> str:
    tool_context.state["student:level"] = level
    tool_context.state["student:topic"] = topic
    return f"Goal Saved: Learning '{topic}' at '{level}' level."

def get_quiz_data(tool_context: ToolContext) -> str:
    topic = tool_context.state.get("student:topic", "General")
    level = tool_context.state.get("student:level", "Beginner")
    return f"Topic: {topic}, Level: {level}"

# --- AGENT ---
registrar = LlmAgent(
    name="edu_registrar",
    model=Gemini(model=MODEL_NAME, retry_options=retry_config),
    description="Backend memory.",
    instruction="Store data and retrieve it.",
    tools=[set_learning_goal, get_quiz_data]
)
# --- API ENDPOINT ---
class RequestModel(BaseModel):
    prompt: str

@app.post("/chat")
async def chat_endpoint(req: RequestModel):
    try:
        # Use the correct method to run the agent
        from google.adk.runners import Runner
        from google.adk.sessions import InMemorySession
        
        # Create a session and runner
        session = InMemorySession()
        runner = Runner(agent=registrar, session=session)
        
        # Run the agent and collect events
        events = []
        async for event in runner.run_async(req.prompt):
            events.append(event)
        
        # Extract the response from the events
        for event in reversed(events):
            if hasattr(event, 'content') and event.content.parts:
                response_text = event.content.parts[0].text
                return {"response": response_text}
        
        return {"response": "No response generated"}
        
    except Exception as e:
        return {"response": f"Error: {str(e)}"}
    
# --- THE CRITICAL STARTUP BLOCK ---
if __name__ == "__main__":
    print("🚀 Registrar Server Running on Port 8001...")
    uvicorn.run(app, host="127.0.0.1", port=8001)