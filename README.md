# Agno Session

This repository contains examples and implementations of AI agents and workflows using the Agno framework. It demonstrates how to build powerful AI applications with natural language processing capabilities.

## Projects

### [SQL Chat with Agno Workflows](sql-chat/README.md)

![SQL Chat Application](https://github.com/vivekpathania/Agno-Session/blob/main/assets/Screenshot%202025-04-19%20at%207.00.43%20PM.png?raw=true)

A natural language SQL chatbot that allows users to query databases using plain English. The application uses Agno's workflow capabilities to process queries through specialized agents.

**Key Features:**
- Natural language to SQL conversion
- Direct, concise answers to database queries
- Streamlit-based user interface
- UV package manager for dependency management

[View SQL Chat README](sql-chat/README.md)

### [Agno CLI Samples](cli-samples/README.md)

A collection of sample implementations demonstrating various Agno agents and workflows, from basic agents to more complex team-based solutions.

**Samples Included:**
- Basic Agent
- Calculator Agent
- Memory Agent
- Agent Team
- Simple Agent

[View CLI Samples README](cli-samples/README.md)

## Getting Started

### Prerequisites

* **UV:** This project uses the UV package manager. Install it by following the instructions on the UV website: [https://astral.sh/uv](https://astral.sh/uv).
* **Python 3.10+:** Ensure you have Python 3.10 or a later version installed.
* **Environment Variables:** Set up the necessary environment variables as described in each project's README.

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/vivekpathania/Agno-Session
   cd Agno-Session
   ```

2. **Install Dependencies with UV:**
   ```bash
   uv sync
   ```
   This command will:
   * Create a virtual environment if one does not exist.
   * Install all the dependencies listed in the `pyproject.toml` file.

3. **Set Up Environment Variables:**
   Create a `.env` file in the project root and add your environment variables as described in each project's README.

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