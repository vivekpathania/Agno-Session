from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get configuration from environment variables
model_name = os.getenv("MODEL_NAME", "gpt-4")
api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API_KEY not found in environment variables")

# Initialize the agent with OpenAI model and DuckDuckGo search tool
agent = Agent(
    model=Groq(id=model_name, api_key=api_key),
    tools=[DuckDuckGoTools()],
    instructions="You are a tech news agent that provides accurate and up-to-date information about technology topics. Use DuckDuckGo search to find the latest information when needed."
)

# Example usage
agent.print_response("What are the latest developments in AI technology?", stream=True)
