import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise SystemExit("GROQ_API_KEY not found in environment. Add it to your .env file.")

model = ChatGroq(model="llama-3.1-70b-versatile", temperature=0)
print(f"Using Groq with llama-3.1-70b-versatile")

def get_weather(city: str) -> str:
    """Get the current weather for a given city."""
    return f"The weather in {city} is too hot to handle, 28 degrees C."

agent = create_react_agent(model=model, tools=[get_weather])

def ask(question: str, show_steps: bool = True) -> None:
    response = agent.invoke({"messages": [HumanMessage(content=question)]})
    print(f"\nQ: {question}")

    if show_steps:
        for msg in response["messages"]:
            if hasattr(msg, "tool_calls") and msg.tool_calls:
                for tc in msg.tool_calls:
                    print(f"   [tool call]   {tc['name']}({tc['args']})")
            elif hasattr(msg, "content") and hasattr(msg, "name"):
                print(f"   [tool result] {msg.content}")

    final_message = response["messages"][-1]
    print(f"A: {final_message.content}")

if __name__ == "__main__":
    ask("What is the weather like in New York?")
    ask("What is scaler company?")