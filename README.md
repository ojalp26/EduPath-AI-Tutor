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
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   echo "GOOGLE_API_KEY=your_api_key_here" > .env
   ```

### Running the Application

1. **Start the Registrar Server** (Terminal 1)
   ```bash
   python server.py
   ```
   *Server runs on: http://127.0.0.1:8001*

2. **Start the Tutor Interface** (Terminal 2)
   ```bash
   adk web . --port 8000
   ```
   *Web interface: http://127.0.0.1:8000*

## 📖 Usage

### Learning Workflow

1. **Topic Selection** - User specifies interest area
2. **Level Assessment** - Beginner, Intermediate, or Advanced
3. **Interactive Teaching** - Step-by-step explanations with examples
4. **Knowledge Assessment** - Context-aware quiz generation with feedback

### Example Interaction
User: I want to learn about machine learning

EduPath: Great! What's your current experience level?

User: Beginner

EduPath: [Provides educational content...]

Would you like to test your understanding with a quiz?

## 📁 Project Structure

edupath/

├── agent.py # Main tutoring agent

├── server.py # Backend registrar agent

├── requirements.txt # Python dependencies

├── .env # Environment variables

└── README.md # Project documentation


## 🛠️ Technical Details

### Technologies Used

- **Backend**: FastAPI, Uvicorn
- **AI Framework**: Google Agent Development Kit (ADK)
- **AI Model**: Gemini 2.0 Flash
- **Session Management**: SQLite

### Key Dependencies

- google-adk
- google-genai
- fastapi
- uvicorn
- python-dotenv
- requests
- pydantic


## 🔧 Configuration

### Environment Variables

Create a `.env` file with:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
Model Configuration
Primary Model: gemini-2.0-flash
Fallback: gemini-flash-latest
```




## 📄 License
This project is licensed under the MIT License.


## 🙏 Acknowledgments
Google ADK team for the agent development framework
FastAPI for the efficient web framework
Gemini AI for content generation capabilities
