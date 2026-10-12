import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise SystemExit("GROQ_API_KEY not found in environment. Add it to your .env file.")

model = ChatGroq(model="openai/gpt-oss-120b", temperature=0)
print(f"Using Groq with openai/gpt-oss-120b")

def get_weather(city: str) -> str:
    """Get the current weather for a given city."""
    return f"The weather in {city} is sunny, 28 degrees C."

def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b

def multiply(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b

def get_population(city: str) -> str:
    """Get the approximate population of a major city."""
    data = {
        "new york": "8.5 million",
        "london": "9 million",
        "bangalore": "13 million",
        "tokyo": "14 million",
    }
    return data.get(city.lower(), f"Sorry, I don't have population data for {city}.")

TOOLS = [get_weather, add, multiply, get_population]

agent = create_react_agent(
    model=model,
    tools=TOOLS,
)

def ask(question: str, show_steps: bool = True) -> None:
    from langchain_core.messages import HumanMessage

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
    ask("What is 25 multiplied by 4?")
    ask("What is 137 plus 568?")
    ask("What is the population of Bangalore?")
    ask("What's the weather in Tokyo, and what is 12 times 12?")
    ask("Who wrote the play Romeo and Juliet?")