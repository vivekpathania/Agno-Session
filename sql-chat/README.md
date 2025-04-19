# SQL Chat with Agno Workflows

This project demonstrates how to build an interactive SQL chatbot using natural language processing (NLP) and Agno's workflow capabilities. It allows users to query an SQL database using natural language and get direct, concise answers.

## Features

* **Natural Language SQL Queries:** Interact with an SQL database using natural language. The chatbot understands your questions and translates them into SQL queries.
* **Agno Workflow Integration:** Leverages Agno's workflow capabilities for structured, multi-agent processing.
* **Specialized Agents:** Uses two specialized agents - a query agent for understanding questions and generating SQL, and a data agent for executing SQL and providing direct answers.
* **Streamlit UI:** Provides a clean, responsive user interface for interacting with the SQL chatbot.
* **UV Package Manager:** Uses UV package manager for dependency management.

## Project Structure

* **`sql_chat_agent.py`:** Contains the SQL workflow implementation with specialized agents.
* **`streamlit_app.py`:** The Streamlit application that provides the user interface.
* **`llm_model.py`:** Utility for selecting the appropriate LLM model based on configuration.
* **`.env`:** Configuration file for environment variables.

## Prerequisites

* **UV:** This project uses the UV package manager. Install it by following the instructions on the UV website: [https://astral.sh/uv](https://astral.sh/uv).
* **Python 3.9+:** Ensure you have Python 3.9 or a later version installed.
* **MCP SQL Server:** You need an MCP SQL server running. You can set it up using the `uvx` command.
* **Database:** An SQL database (e.g., MySQL, PostgreSQL) with some data.
* **Environment Variables:** Set the following environment variables in a `.env` file in the project root:
  * `MODEL_API_KEY`: Your API key for the LLM provider (OpenAI, Anthropic, or Groq).
  * `MODEL_ID`: The model ID to use (e.g., `claude-3-5-sonnet-20241022`, `gpt-4o`, `llama-3.3-70b-versatile`).
  * `DB_HOST`: The hostname or IP address of your database server.
  * `DB_USER`: The username for your database.
  * `DB_PASSWORD`: The password for your database.
  * `DB_NAME`: The name of your database.

## Setup and Installation (using UV)

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd sql-chat
   ```

2. **Install Dependencies with UV:**
   ```bash
   uv sync
   ```
   This command will:
   * Create a virtual environment if one does not exist.
   * Install all the dependencies listed in the `pyproject.toml` file.

3. **Create `.env` File:**
   Create a `.env` file in the project root and add your environment variables:
   ```
   DB_HOST=your_db_host
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_NAME=your_db_name
   MODEL_API_KEY=your_api_key
   MODEL_ID=your_model_id
   ```

## Running the Application

1. **Activate the Virtual Environment:**
   UV will create a `.venv` folder in your project.
   ```bash
   source .venv/bin/activate  # On Linux/macOS
   .venv\Scripts\activate     # On Windows
   ```

2. **Run the Streamlit App:**
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Access the App:**
   Open your web browser and go to the URL provided in the terminal (usually `http://localhost:8501`).

## Usage

1. **Ask Questions:** Type your questions about the database in natural language (e.g., "List all employees," "What are the top-selling products?").
2. **View Results:** The chatbot will respond with a direct answer to your query.

## Example Queries

* **Schema Questions:**
  * "What tables are in the database?"
  * "Show me the structure of the customers table"
  * "What are the relationships between tables?"

* **Query Questions:**
  * "How many orders were placed in 2023?"
  * "List all customers from California"
  * "What are the top 5 products by sales?"

* **Analysis Questions:**
  * "What are the sales trends over the past year?"
  * "Which customers have the highest lifetime value?"
  * "Compare the performance of different product categories"

## Key Components

* **`sql_chat_agent.py`:**
  * Defines the `SQLWorkflow` class that orchestrates the query and data agents.
  * The query agent understands natural language and generates SQL queries.
  * The data agent executes the SQL and provides direct, concise answers.

* **`streamlit_app.py`:**
  * The main Streamlit application.
  * Provides the user interface for the chatbot.
  * Uses `st.session_state` to persist chat messages.
  * Formats responses to make them stand out.

## Related Projects

For a more advanced dashboard generator that builds on this concept, check out the [MCP SQL Chatbot & Dashboard](https://github.com/vivekpathania/ai-experiments/blob/main/mcp-agent-experiment/README.md) project.

## Why UV?

UV is a modern Python package manager that offers significant advantages over pip:

* **Speed:** UV is 10-100x faster than pip for package installation.
* **Reliability:** UV provides more reliable dependency resolution.
* **Compatibility:** UV is fully compatible with existing Python projects.
* **Simplicity:** UV has a simpler, more intuitive interface.

For more information about UV and its benefits, check out this article: [From pip to lightning: How UV opened my eyes to better Python workflows](https://medium.com/@viveksinghpathania/from-pip-to-lightning-how-uv-opened-my-eyes-to-better-python-workflows-dfa50e8a5893).

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## License

MIT
