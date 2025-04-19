from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
model_name = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")
api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API_KEY not found in environment variables")

# Create a simple agent
agent = Agent(
    model=Groq(id=model_name, api_key=api_key),
    instructions="You are a helpful assistant that provides clear and concise answers."
)

# Example usage
if __name__ == "__main__":
    # Ask a simple question
    agent.print_response("What is artificial intelligence?", stream=True) 