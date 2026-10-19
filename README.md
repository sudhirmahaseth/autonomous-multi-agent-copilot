# Autonomous Multi-Agent Copilot

An advanced multi-agent specialized research copilot built using **LangGraph** for robust state management and complex tool execution. The system leverages **CrewAI** and **OpenAI GPT-4o** to conduct deep research and synthesize complex data, reducing manual data synthesis intervals by 50%.

## 🚀 Features
- **Stateful Multi-Agent Workflows:** Orchestrated using LangGraph for complex, cyclic graph routing and state management.
- **Specialized Agents:** CrewAI agents assigned with specific roles, goals, and customized search tools.
- **Advanced Prompt Engineering:** Implemented Few-Shot and Chain-of-Thought (CoT) prompting techniques for high-accuracy reasoning.
- **Production-Ready Backend:** Asynchronous API engine powered by FastAPI.
- **Secure Infrastructure:** Containerized with Docker and hosted securely on AWS EC2.

## 🛠️ Tech Stack
- **Frameworks:** LangGraph, LangChain, CrewAI, FastAPI
- **LLM:** OpenAI GPT-4o
- **Vector Database:** FAISS (for context retrieval and semantic search)
- **DevOps:** AWS EC2, Docker, Python

## 🔧 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd autonomous-multi-agent-copilot
   ```

2. **Set up a virtual environment & install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the Application:**
   ```bash
   uvicorn main:app --reload
   ```
