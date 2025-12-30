# Building Agentic AI

A comprehensive practice repository for developing and experimenting with agentic AI systems using various frameworks and tools.

## 🚀 Project Overview

This repository contains multiple AI agent implementations exploring different use cases, frameworks, and integration patterns. Each project demonstrates practical applications of agentic AI systems with real-world scenarios.

## 📁 Project Structure

### 🏥 Health Agent System
**Location:** `health-agent-system/`

Multi-agent health and nutrition system with specialized agents:
- **Recipe Scout Agent**: Researches and lists health-focused recipes
- **Clinical Reviewer Agent**: Critically reviews and ranks recipes for safety
- **Technologies**: LangChain, Google Gemini, DuckDuckGo Search, CrewAI, PhiData
- **Notebooks**:
  - `health-agents.ipynb` - Core multi-agent implementation
  - `health-agents-using-crew-agent.ipynb` - CrewAI implementation
  - `fitness-agents-using-phidata.ipynb` - PhiData framework
  - `healt-agents-phidata-gorq.ipynb` - PhiData with Groq integration

### 🌤️ Weather Agents
**Location:** `weather-agents/`

Weather information and analysis agents:
- **Technologies**: LangChain, Google Gemini, DuckDuckGo Search
- **Features**: Real-time weather data retrieval and analysis
- **Notebook**: `weather-agent.ipynb`

### 🔧 Kiro Agent with MCP
**Location:** `kiro-agent-with-mcp/`

Model Context Protocol (MCP) integration with MongoDB:
- **Technologies**: FastMCP, PyMongo, MongoDB
- **Features**: User management system with CRUD operations
- **Server**: `server.py` - MCP server implementation
- **Database**: MongoDB integration for persistent storage

## 🛠️ Technologies & Frameworks

### Core AI Frameworks
- **LangChain**: Agent orchestration and tool integration
- **CrewAI**: Multi-agent collaboration framework
- **PhiData**: Modern AI agent framework
- **FastMCP**: Model Context Protocol implementation

### Language Models
- **Google Gemini 2.5 Flash**: Primary LLM for most agents
- **Groq Cloud**: Alternative LLM provider integration

### Tools & Integrations
- **DuckDuckGo Search**: Web search capabilities
- **MongoDB**: Database storage and management
- **Python Environment**: Virtual environments for each project

## 🚦 Getting Started

### Prerequisites
- Python 3.8+
- MongoDB (for MCP projects)
- API keys for:
  - Google Gemini AI
  - Groq Cloud (optional)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd building-agentic-ai
```

2. Set up individual project environments:

**For Health Agents:**
```bash
cd health-agent-system
python -m venv myenv
myenv\Scripts\activate  # Windows
source myenv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

**For Weather Agents:**
```bash
cd weather-agents
python -m venv myenv
myenv\Scripts\activate  # Windows
source myenv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

**For MCP Agent:**
```bash
cd kiro-agent-with-mcp
pip install -r requirements.txt
```

3. Configure environment variables:
Create `.env` files in respective project directories with:
```
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key  # Optional
```

## 🎯 Usage Examples

### Health Agent System
Run the Jupyter notebooks to see multi-agent collaboration:
- Recipe research and clinical review
- Blood sugar stability analysis
- Nutritional safety assessments

### Weather Agents
Weather information retrieval and analysis with real-time data.

### MCP Agent
Start the MCP server:
```bash
cd kiro-agent-with-mcp
python server.py
```

Available operations:
- Add users
- Update user information
- Delete users
- Retrieve user data

## 🔄 Agent Patterns Demonstrated

1. **Sequential Agent Workflow**: Health agents with handoff between Recipe Scout and Clinical Reviewer
2. **Tool Integration**: Web search, database operations, and API integrations
3. **Multi-Framework Comparison**: Same use case implemented across different frameworks
4. **Protocol Integration**: MCP for standardized agent communication

## 📝 Key Features

- **Multi-Agent Orchestration**: Coordinated agent workflows
- **Framework Flexibility**: Multiple AI frameworks for comparison
- **Real-World Applications**: Practical use cases in health, weather, and data management
- **Extensible Architecture**: Easy to add new agents and capabilities
- **Protocol Standards**: MCP integration for interoperability

## 🤝 Contributing

Feel free to contribute by:
- Adding new agent implementations
- Exploring different frameworks
- Improving existing agents
- Adding new use cases

## 📄 License

This project is for educational and practice purposes.