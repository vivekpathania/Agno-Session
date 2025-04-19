import os
import asyncio
import streamlit as st
from dotenv import load_dotenv
from sql_chat_agent import run_sql_workflow

# Load environment variables
load_dotenv()

# Set page configuration
st.set_page_config(
    page_title="SQL Chat Assistant",
    page_icon="💬",
    layout="wide",
)

# Add custom CSS
st.markdown("""
<style>
    .stTextInput>div>div>input {
        font-size: 16px;
    }
    .stTextArea>div>div>textarea {
        font-size: 16px;
    }
    .main .block-container {
        padding-top: 2rem;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .chat-message.user {
        background-color: #f0f2f6;
    }
    .chat-message.assistant {
        background-color: #e6f7ff;
    }
    .chat-message .content {
        margin-top: 0.5rem;
    }
    .agent-badge {
        display: inline-block;
        padding: 0.25rem 0.5rem;
        border-radius: 0.25rem;
        font-size: 0.75rem;
        font-weight: bold;
        margin-right: 0.5rem;
    }
    .query-agent-badge {
        background-color: #007bff;
        color: white;
    }
    .data-agent-badge {
        background-color: #28a745;
        color: white;
    }
    .workflow-badge {
        background-color: #fd7e14;
        color: white;
    }
    .sql-query {
        background-color: #f8f9fa;
        padding: 0.75rem;
        border-radius: 0.25rem;
        font-family: monospace;
        margin: 0.5rem 0;
        border-left: 3px solid #007bff;
    }
    .response-value {
        font-size: 1.2rem;
        font-weight: bold;
        color: #28a745;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title and description
st.title("💬 SQL Chat Assistant")
st.markdown("""
This assistant helps you interact with your MySQL database using natural language.
Ask questions about your data, and the assistant will translate them into SQL queries and provide direct answers.
""")

# Sidebar with information
with st.sidebar:
    st.header("About")
    st.markdown("""
    This application uses an Agno workflow with two specialized agents:
    
    - **Query Understanding Agent**: Understands your questions and generates SQL queries
    - **Data Execution Agent**: Executes the SQL and provides direct answers
    
    The workflow orchestrates these agents to provide a seamless experience.
    """)
    
    st.header("Database Info")
    st.markdown(f"""
    - **Host:** {os.getenv('DB_HOST')}
    - **Database:** {os.getenv('DB_NAME')}
    - **User:** {os.getenv('DB_USER')}
    """)
    
    st.header("Model Info")
    st.markdown(f"""
    - **Model:** {os.getenv('MODEL_ID', 'claude-3-5-sonnet-20241022')}
    """)
    
    st.header("Example Queries")
    st.markdown("""
    **Schema Questions:**
    - "What tables are in the database?"
    - "Show me the structure of the customers table"
    - "What are the relationships between tables?"
    
    **Query Questions:**
    - "How many orders were placed in 2023?"
    - "List all customers from California"
    - "What are the top 5 products by sales?"
    
    **Analysis Questions:**
    - "What are the sales trends over the past year?"
    - "Which customers have the highest lifetime value?"
    - "Compare the performance of different product categories"
    """)

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if "agent_type" in message:
            st.markdown(f'<span class="agent-badge {message["agent_type"]}-badge">{message["agent_type"].replace("-", " ").capitalize()}</span>', unsafe_allow_html=True)
        
        # Display SQL query if available
        if "sql_query" in message and message["sql_query"]:
            st.markdown("**SQL Query:**")
            st.markdown(f'<div class="sql-query">{message["sql_query"]}</div>', unsafe_allow_html=True)
        
        # Display the content
        if message["role"] == "assistant":
            st.markdown(f'<div class="response-value">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask a question about your database..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # Run the SQL workflow and capture the response
        async def get_response():
            response = await run_sql_workflow(prompt)
            return response
        
        # Run the async function and get the response
        response = asyncio.run(get_response())
        
        # Add assistant response to chat history
        st.session_state.messages.append({
            "role": "assistant", 
            "content": response,
            "agent_type": "data-agent"
        })
        
        # Display the response with agent badge
        st.markdown(f'<span class="agent-badge data-agent-badge">Data Agent</span>', unsafe_allow_html=True)
        message_placeholder.markdown(f'<div class="response-value">{response}</div>', unsafe_allow_html=True)

# Add a clear button
if st.button("Clear Chat History"):
    st.session_state.messages = []
    st.experimental_rerun() 