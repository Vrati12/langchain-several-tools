import langchain
import os
from dotenv import load_dotenv, find_dotenv
from langchain.agents import create_agent

print("LangChain version:", langchain.__version__)

load_dotenv(find_dotenv(), override=True)

PROVIDER = "groq"

if PROVIDER == "groq":
    MODEL = "groq:llama-3.3-70b-versatile"
    REQUIRED_KEY = "GROQ_API_KEY"
elif PROVIDER == "gemini":
    MODEL = "google_genai:gemini-2.0-flash"
    REQUIRED_KEY = "GOOGLE_API_KEY"
else:
    MODEL = "openai:gpt-4o-mini"
    REQUIRED_KEY = "OPENAI_API_KEY"

key = os.environ.get(REQUIRED_KEY)
if not key:
    raise SystemExit(
        f"{REQUIRED_KEY} not found in environment. "
        f"Add it to your .env for provider '{PROVIDER}'."
    )
print(f"Provider={PROVIDER}  Model={MODEL}  Key={key[:6]}...{key[-4:]}")

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

agent = create_agent(
    model=MODEL,
    tools=TOOLS,
    system_prompt=(
        "You are a helpful assistant. Use the available tools when needed. "
        "Always state the final result clearly and completely in your answer."
    ),
)

def ask(question: str, show_steps: bool = True) -> None:
    response = agent.invoke({"messages": [{"role": "user", "content": question}]})
    print(f"\nQ: {question}")

    if show_steps:
        for msg in response["messages"]:
            if msg.type == "ai" and getattr(msg, "tool_calls", None):
                for tc in msg.tool_calls:
                    print(f"   [tool call]   {tc['name']}({tc['args']})")
            elif msg.type == "tool":
                print(f"   [tool result] {msg.content}")

    print(f"A: {response['messages'][-1].content}")

if __name__ == "__main__":
    ask("What is the weather like in New York?")
    ask("What is 25 multiplied by 4?")
    ask("What is 137 plus 568?")
    ask("What is the population of Bangalore?")
    ask("What's the weather in Tokyo, and what is 12 times 12?")
    ask("Who wrote the play Romeo and Juliet?")