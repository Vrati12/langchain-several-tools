# LangChain Several Tools

LangChain-based AI agents demonstrating tool calling with multiple capabilities including weather lookup, calculations, and population data.

## Overview

This project showcases how to build intelligent agents that can autonomously select and use the right tools to answer questions.

## Files

- `a.py` - Multi-tool agent (weather, add, multiply, population)
- `b.py` - Single-tool agent (weather)

## Features

### Multi-Tool Agent (a.py)
- **Weather Lookup** - Get current weather for any city
- **Mathematical Operations** - Addition and multiplication
- **Population Data** - City population information
- **Visible Tool Calls** - See exactly which tools the agent uses

### Single-Tool Agent (b.py)
- **Weather Queries** - Simple weather information retrieval
- **Step-by-step Execution** - Transparent tool calling process

## Technologies Used

- **LangChain** - Agent framework
- **LangGraph** - Agent orchestration
- **Groq API** - Free, fast LLM inference

## Setup

1. Install dependencies:
```bash
pip install langchain langgraph langchain-groq python-dotenv
```

2. Create `.env` file:
```
GROQ_API_KEY=your_api_key_here
```

Get your free API key from: https://console.groq.com

3. Run the agents:
```bash
python a.py  # Multi-tool agent
python b.py  # Single-tool agent
```

## How It Works

The agents use LangChain's tool calling capabilities:
1. Receive a user question
2. Analyze which tool(s) are needed
3. Call the appropriate function(s)
4. Generate a natural language response

## Example Queries

**Multi-tool agent (a.py):**
- "What is the weather like in New York?"
- "What is 25 multiplied by 4?"
- "What is the population of Bangalore?"
- "What's the weather in Tokyo, and what is 12 times 12?"

**Single-tool agent (b.py):**
- "What is the weather like in New York?"
- "How's the weather in London?"

## Important Notes

### Model Configuration
⚠️ **Groq frequently deprecates older models.** If you encounter a `model_decommissioned` or `model_not_found` error:

1. Visit https://console.groq.com/docs/models to see currently available models
2. Update the model name in both `a.py` and `b.py`:
   ```python
   model = ChatGroq(model="YOUR_CURRENT_MODEL_NAME", temperature=0)
   ```

**Recommended models** (as of late 2024):
- `llama-3.1-70b-versatile` - Best for tool calling
- `llama-3.1-8b-instant` - Faster, good for simple tasks  
- `gemma-7b-it` - Alternative option

### Dependencies
This code uses LangChain's agent API (LangGraph). Ensure you have compatible versions:
```bash
pip install langchain langgraph langchain-groq python-dotenv
```
