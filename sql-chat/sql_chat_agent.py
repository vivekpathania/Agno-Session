import os
import asyncio
from typing import Dict, Any

from dotenv import load_dotenv
from agno.agent import Agent, RunResponse
from agno.tools.mcp import MCPTools
from agno.workflow import Workflow, RunEvent
from agno.utils.log import logger
from agno.utils.pprint import pprint_run_response
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from llm_model import get_model

# Load environment variables
load_dotenv()

class SQLWorkflow(Workflow):
    """
    A workflow that processes natural language SQL queries using two specialized agents.
    """
    description: str = "A workflow that converts natural language to SQL and executes it"
    
    # Define the agents as class attributes
    query_agent = Agent(
        model=get_model(
            os.getenv('MODEL_ID', 'claude-3-5-sonnet-20241022'),
            os.getenv('MODEL_API_KEY')
        ),
        description="""You are a SQL expert who understands natural language queries and converts them to SQL.
        Your job is to:
        1. Understand the user's question
        2. Use the MCP tool to fetch the database schema
        3. Write appropriate SQL queries to answer the question
        4. Return both the SQL query and a brief explanation of what it does
        """,
        markdown=True
    )
    
    data_agent = Agent(
        model=get_model(
            os.getenv('MODEL_ID', 'claude-3-5-sonnet-20241022'),
            os.getenv('MODEL_API_KEY')
        ),
        description="""You are a data analyst who executes SQL queries and provides concise, direct answers.
        Your job is to:
        1. Take the SQL query from the previous agent
        2. Use the MCP tool to execute the query and fetch the results
        3. Provide ONLY the direct answer to the question without additional commentary
        4. Format numbers appropriately (e.g., use commas for thousands)
        5. Do NOT add explanations, context, or suggestions for follow-up queries
        """,
        instructions="""When responding to queries:
        - Give ONLY the direct answer to the question
        - Do NOT add explanations or context
        - Do NOT suggest follow-up queries
        - Do NOT add commentary about the data
        - Format numbers appropriately
        - Keep responses extremely concise
        """,
        markdown=True
    )
    
    def __init__(self, session: ClientSession):
        super().__init__()
        self.session = session
        # Initialize MCP tools for both agents
        mcp_tools = MCPTools(session=session)
        self.query_agent.tools = [mcp_tools]
        self.data_agent.tools = [mcp_tools]
    
    # Write the logic in the `run()` method
    def run_workflow(self, user_query: str) -> RunResponse:
        logger.info(f"Processing query: '{user_query}'")
        
        # Step 1: Generate SQL from natural language
        logger.info("Step 1: Generating SQL from natural language")
        query_response = self.query_agent.run(user_query)
        
        # Get the SQL query from the query agent
        sql_query = query_response.content
        
        # Step 2: Execute SQL and provide natural language response
        logger.info("Step 2: Executing SQL and providing response")
        execution_prompt = f"Execute this SQL query and provide a direct answer: {sql_query}"
        data_response = self.data_agent.run(execution_prompt)
        
        # Return the final response
        return RunResponse(
            event=RunEvent.workflow_completed,
            content=data_response.content
        )


async def run_sql_workflow(message: str) -> str:
    """Run the SQL workflow with the given message and return the response."""
    # Get database configuration from environment
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_NAME')

    # Initialize the MCP server
    server_params = StdioServerParameters(
        command="uvx",
        args=[
            "mcp-sql-server",
            "--db-host", db_host,
            "--db-user", db_user,
            "--db-password", db_password,
            "--db-database", db_name
        ],
    )

    # Create a client session to connect to the MCP server
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Create the workflow with the session
            workflow = SQLWorkflow(session=session)
            
            # Run the workflow and get the response
            response = workflow.run_workflow(message)
            
            # Return the content from the response
            return response.content


if __name__ == "__main__":
    # Example usage
    query = "Give me the total sales for q3"
    response = asyncio.run(run_sql_workflow(query))
    print(response) 