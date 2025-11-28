# EduPath - AI-Powered Educational Assistant

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![Google ADK](https://img.shields.io/badge/Google-ADK-orange.svg)

An intelligent educational assistant that provides personalized learning experiences through AI-powered tutoring and adaptive assessment systems.

## 🎯 Overview

EduPath is a sophisticated AI tutoring system that uses a multi-agent architecture to deliver personalized educational content. The system understands user learning preferences, provides tailored explanations, and generates context-aware quizzes to reinforce learning.

## ✨ Features

- 🤖 **Dual-Agent Architecture** - Separate agents for tutoring and data management
- 🎓 **Personalized Learning** - Adapts content based on topic and proficiency level  
- 📝 **Interactive Quizzes** - Generates context-aware assessments with detailed feedback
- 💾 **State Persistence** - Maintains learning progress across sessions
- 🛠️ **Tool-Based Communication** - Seamless integration between system components
- 🎨 **Clean UI** - Web-based interface for easy interaction

## 🏗️ System Architecture

### Agent Structure

<img width="585" height="296" alt="image" src="https://github.com/user-attachments/assets/b9922a36-2d86-44d8-a0cf-20a8ec2dc572" />


### Core Components

#### EduTutor Agent (`agent.py`)
- Primary user interaction interface
- Content generation and teaching logic  
- Quiz presentation and evaluation
- Tool coordination

#### EduRegistrar Agent (`server.py`)
- Data persistence and state management
- Learning goal storage
- Session management
- REST API endpoints

#### Bridge Tools
- `call_registrar_server()` - Inter-agent communication
- `set_learning_goal()` - Store user preferences
- `get_quiz_data()` - Retrieve learning context

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google Gemini API key
- Required packages (see requirements.txt)

### Installation

1. **Clone the repository**
   ```
   git clone https://github.com/yourusername/edupath.git
   cd edupath```

2. **Set up virtual environment**
```
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate```

### Install dependencies:

```
pip install -r requirements.txt
```

### Running the Application
Start the Registrar Server (Terminal 1)

bash
python server.py
Server runs on: http://127.0.0.1:8001

Start the Tutor Interface (Terminal 2)

bash
adk web . --port 8000
Web interface: http://127.0.0.1:8000

## 📖 Usage
Learning Workflow
Topic Selection

User specifies interest area (e.g., "Python programming")

System determines appropriate starting point

Level Assessment

Beginner, Intermediate, or Advanced

Tailors content complexity accordingly

Interactive Teaching

Step-by-step explanations

Practical examples and analogies

Progressive concept building

Knowledge Assessment

Context-aware quiz generation

Immediate feedback and explanations

Progress tracking

Example Interaction
text
User: I want to learn about machine learning
EduPath: Great! What's your current experience level - Beginner, Intermediate, or Advanced?

User: Beginner  
EduPath: [Stores preference] Let me explain machine learning basics...
[Provides educational content]
Would you like to test your understanding with a quiz?
📁 Project Structure
text
edupath/
├── agent.py              # Main tutoring agent with web interface
├── server.py             # Backend registrar agent with FastAPI
├── requirements.txt      # Python dependencies
├── .env                 # Environment variables (API keys)
└── README.md            # Project documentation
🛠️ Technical Details
Technologies Used
Backend: FastAPI, Uvicorn

AI Framework: Google Agent Development Kit (ADK)

AI Model: Gemini 2.0 Flash

Session Management: SQLite

Communication: HTTP REST API, Tool-based integration

Key Dependencies
text
google-adk
google-genai
fastapi
uvicorn
python-dotenv
requests
pydantic
🔧 Configuration
Environment Variables
Create a .env file with:

env
GOOGLE_API_KEY=your_gemini_api_key_here
Model Configuration
Primary Model: gemini-2.0-flash

Fallback: gemini-flash-latest

Retry Configuration: 5 attempts with exponential backoff

🎨 Customization
Adding New Subjects
Modify the instruction prompt in agent.py to include new domains:

python
instruction="""
You are EduPath - now expanded to include:
- Computer Science
- Mathematics  
- History
- [Your Subject Here]
...
"""
Extending Tools
Add new tools to server.py:

python
def new_educational_tool(tool_context: ToolContext, parameter: str) -> str:
    # Your custom logic here
    return "Tool execution result"
🤝 Contributing
We welcome contributions! Please feel free to submit pull requests for:

New educational domains

Enhanced quiz formats

Additional tool integrations

UI improvements

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Google ADK team for the agent development framework

FastAPI for the efficient web framework

Gemini AI for the content generation capabilities
