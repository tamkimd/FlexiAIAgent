# 🌟 FlexiAIAgent

## 🚀 Overview

**FlexiAIAgent** is a powerful and modular AI agent supporting multiple **local and cloud-based language models (LLMs)**. Designed for flexibility and efficiency, it seamlessly integrates **Ollama** for local models, with future support for **ChatGPT, Gemini**, and more.

---

## 🔥 Key Features

✅ **Multi-LLM Support** – Works with both local (Ollama) and cloud-based models.  
✅ **Custom Tools** – Easily extend functionality with your own tools.  
✅ **Quick Validation & Environment Management** – Uses **[Pydantic](https://docs.pydantic.dev/latest/)** for validation and settings management.  
✅ **Fast Dependency Management** – Uses **[uv](https://docs.astral.sh/uv/)** for seamless package management.  
✅ **Code Linting & Formatting** – Uses **[ruff](https://docs.astral.sh/ruff/)** for clean code.  
✅ **Modular & Scalable** – Build custom AI apps without hassle.

---

## 📖 Table of Contents

- [🌟 FlexiAIAgent](#-flexiaiagent)
  - [🚀 Overview](#-overview)
  - [🔥 Key Features](#-key-features)
  - [📖 Table of Contents](#-table-of-contents)
  - [🔧 Installation](#-installation)
    - [1️⃣ Install `uv`](#1️⃣-install-uv)
      - [**MacOS \& Linux**](#macos--linux)
      - [**Windows**](#windows)
    - [2️⃣ Install `Ollama`](#2️⃣-install-ollama)
    - [3️⃣ Download LLM Models](#3️⃣-download-llm-models)
  - [🚀 Usage](#-usage)
  - [🛠️ Adding Custom Tools](#️-adding-custom-tools)
  - [🧹 Code Linting with `ruff`](#-code-linting-with-ruff)
  - [🤝 Contributing](#-contributing)
  - [🔮 Future Roadmap](#-future-roadmap)
  - [📜 License](#-license)

---

## 🔧 Installation

### 1️⃣ Install `uv`

To efficiently manage dependencies, install `uv` using one of the following methods:

#### **MacOS & Linux**

Using Homebrew (recommended):

```bash
brew install uv
```

Using the installation script:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### **Windows**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2️⃣ Install `Ollama`

Follow the official installation guide at [Ollama](https://ollama.com/).

### 3️⃣ Download LLM Models

To install a model, run:

```bash
ollama pull gemma2:latest
```

Explore more models at the [Ollama Library](https://ollama.com/library).

---

## 🚀 Usage

1️⃣ **Clone the repository:**

```bash
git clone https://github.com/tamkimd/FlexiAIAgent.git
cd FlexiAIAgent
```

2️⃣ **Set up python and dependencies:**

```bash
uv sync
```

3️⃣ **Configure environment variables:**
Create a `.env` file in the root directory:

```plaintext
SERPER_API_KEY=your_api_key_here  # Required if using search tools
```

4️⃣ **Run the demo:**

```bash
uv run demo.py
```

---

## 🛠️ Adding Custom Tools

FlexiAIAgent is **modular and extendable**. To add a custom tool:

1️⃣ **Create a new Python file** in the `tools` directory.  
2️⃣ **Define your tool** as a class that **inherits from `BaseTool`**.  
3️⃣ **Write a clear and descriptive docstring** so the AI agent understands its functionality.  
4️⃣ **Register your tool** in the agent configuration.  
5️⃣ **Run the application** – your tool is now available!  

This modular system makes it easy to customize and expand FlexiAIAgent.

---

## 🧹 Code Linting with `ruff`

Ensure code quality using `ruff`. Install and run it with:

```bash
uv tool install ruff
uv run ruff check --fix
uv run ruff format
```

Refer to the [ruff documentation](https://docs.astral.sh/ruff/) for details.

---

## 🤝 Contributing

Contributions are welcome! Follow these steps:

1️⃣ Create a branch (`feature/xyz`)  
2️⃣ Commit and push changes  
3️⃣ Open a pull request!

---

## 🔮 Future Roadmap

🚀 **Upcoming Features & Improvements:**

- [ ]  **Cloud-Based LLM Support** (ChatGPT, Gemini, etc.)  
- [ ]  **Multi-Agent Collaboration Features**  

💡 Have a feature suggestion? Open an issue or contribute!

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---
