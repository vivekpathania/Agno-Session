from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import os

class ResearchAnalysisTeam:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        self.model_name = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")
        self.api_key = os.getenv("API_KEY")
        
        if not self.api_key:
            raise ValueError("API_KEY not found in environment variables")
            
        # Initialize agents
        self.researcher = self._create_researcher()
        self.analyst = self._create_analyst()
        self.team = self._create_team()
        
    def _create_researcher(self):
        """Create the research agent"""
        return Agent(
            name="Researcher",
            role="Search and gather information",
            model=Groq(id=self.model_name, api_key=self.api_key),
            tools=[DuckDuckGoTools()],
            instructions="You are a research assistant. Search the web for accurate and relevant information."
        )
        
    def _create_analyst(self):
        """Create the financial analyst agent"""
        return Agent(
            name="Analyst",
            role="Analyze financial data",
            model=Groq(id=self.model_name, api_key=self.api_key),
            tools=[YFinanceTools(stock_price=True, analyst_recommendations=True)],
            instructions="You are a financial analyst. Analyze stock data and provide insights."
        )
        
    def _create_team(self):
        """Create the team coordinator"""
        return Agent(
            team=[self.researcher, self.analyst],
            model=Groq(id=self.model_name, api_key=self.api_key),
            instructions="You are a team coordinator. Use the researcher to gather information and the analyst to analyze financial data."
        )
        
    def analyze_company(self, company_name: str, stream: bool = True):
        """Analyze a company using the team"""
        query = f"Tell me about {company_name}'s latest developments and analyze its stock performance."
        return self.team.print_response(query, stream=stream)

# Example usage
if __name__ == "__main__":
    # Create the team
    team = ResearchAnalysisTeam()
    
    # Analyze a company
    team.analyze_company("Apple") 