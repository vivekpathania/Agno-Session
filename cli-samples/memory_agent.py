from agno.agent import Agent
from agno.run.response import RunResponse
from agno.models.groq import Groq
from dotenv import load_dotenv
import os

class MemoryAgent:
    def __init__(self):
        load_dotenv()
        model_name = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")
        api_key = os.getenv("API_KEY")
        
        if not api_key:
            raise ValueError("API_KEY not found in environment variables")
            
        self.agent = Agent(
            model=Groq(id=model_name, api_key=api_key),
            # Enable session memory
            add_history_to_messages=True,
            # Number of historical responses to keep in memory
            num_history_responses=5,
            instructions="You are a helpful assistant with session memory. You can remember the current conversation and use that context to provide better responses."
        )
        
    def chat(self, query: str, stream=True) -> RunResponse:
        """Chat with the agent while maintaining session memory"""
        return self.agent.print_response(query, stream=stream)
        
    def get_session_history(self):
        """Get the current session's conversation history"""
        return [m.model_dump(include={"role", "content"}) for m in self.agent.memory.messages]
        
    def clear_session(self):
        """Clear the current session's memory"""
        self.agent.memory.messages = []
        print("Session memory cleared!")

# Example usage
if __name__ == "__main__":
    mem = MemoryAgent()
    
    # First interaction
    mem.chat("My name is vivek")
    print("\nSession History:")
    print(mem.get_session_history())
    
    # Second interaction - agent remembers the context
    mem.chat("What is my name?")
    print("\nSession History:")
    print(mem.get_session_history())
    
    # Clear session
    mem.clear_session()
    print("\nAfter clearing session:")
    print(mem.get_session_history())