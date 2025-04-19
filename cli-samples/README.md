# Agno CLI Samples

This repository contains sample implementations of various Agno agents and workflows, demonstrating how to use the Agno framework for building AI-powered applications.

## Project Structure

* **`basic_agent.py`:** A simple agent implementation with basic functionality.
* **`calculator_agent.py`:** An agent that performs mathematical calculations.
* **`memory_agent.py`:** An agent that demonstrates memory capabilities.
* **`agent_team.py`:** An implementation of a team of agents working together.
* **`simple_agent.py`:** A streamlined agent implementation.

## Prerequisites

* **UV:** This project uses the UV package manager. Install it by following the instructions on the UV website: [https://astral.sh/uv](https://astral.sh/uv).
* **Python 3.10+:** Ensure you have Python 3.10 or a later version installed.
* **Environment Variables:** Set the following environment variables in a `.env` file in the project root:
  * `MODEL_API_KEY`: Your API key for the LLM provider (OpenAI, Anthropic, or Groq).
  * `MODEL_ID`: The model ID to use (e.g., `claude-3-5-sonnet-20241022`, `gpt-4o`, `llama-3.3-70b-versatile`).

## Setup and Installation (using UV)

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/vivekpathania/Agno-Session
   cd cli-samples
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
   MODEL_API_KEY=your_api_key
   MODEL_ID=your_model_id
   ```

## Running the Samples

### Basic Agent

```bash
python basic_agent.py
```

This will run a simple agent that demonstrates basic Agno functionality.

### Calculator Agent

```bash
python calculator_agent.py
```

This will run an agent that can perform mathematical calculations.

### Memory Agent

```bash
python memory_agent.py
```

This will run an agent that demonstrates memory capabilities.

### Agent Team

```bash
python agent_team.py
```

This will run a team of agents working together to solve a problem.

### Simple Agent

```bash
python simple_agent.py
```

This will run a streamlined agent implementation.

## Dependencies

The project uses the following main dependencies:

* **agno>=1.3.3:** The Agno framework for building AI agents and workflows.
* **dotenv>=0.9.9:** For loading environment variables from a `.env` file.
* **duckduckgo-search>=8.0.1:** For web search capabilities.
* **groq>=0.22.0:** For using Groq models.
* **yfinance>=0.2.55:** For fetching financial data.

## Why UV?

UV is a modern Python package manager that offers significant advantages over pip:

* **Speed:** UV is 10-100x faster than pip for package installation.
* **Reliability:** UV provides more reliable dependency resolution.
* **Compatibility:** UV is fully compatible with existing Python projects.
* **Simplicity:** UV has a simpler, more intuitive interface.

For more information about UV and its benefits, check out this article: [From pip to lightning: How UV opened my eyes to better Python workflows](https://medium.com/@viveksinghpathania/from-pip-to-lightning-how-uv-opened-my-eyes-to-better-python-workflows-dfa50e8a5893).

## Related Projects

For a more advanced SQL chatbot that builds on these concepts, check out the [SQL Chat with Agno Workflows](https://github.com/vivekpathania/Agno-Session/tree/main/sql-chat) project.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## License

MIT
