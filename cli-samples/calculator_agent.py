from agno.agent import Agent
from agno.models.groq import Groq
from custom_tool import CalculatorTool
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def add_tool( a: float, b: float) -> float:
        """Add two numbers together"""
        print(f"Adding {a} and {b}")
        return f"{a + b}"

# Get configuration from environment variables
model_name = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")
api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API_KEY not found in environment variables")

# Initialize the agent with Groq model and Calculator tool
agent = Agent(
    model=Groq(id=model_name, api_key=api_key),
    tools=[add_tool],
    show_tool_calls=True,
    
    instructions="You are a helpful assistant that can perform calculations. Use the calculator tool to perform arithmetic operations when needed."
)

# Example usage
agent.print_response("What is 5 + 13?", stream=True) 