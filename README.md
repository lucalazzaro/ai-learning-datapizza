AI Learning Crew – Datapizza Edition

A minimalistic multi-agent system that generates a personalized study plan to become an AI/ML Engineer, built with Datapizza AI.

This project mirrors the simplicity and elegance of datapizza-buonanotte:
few files, clear modules, smart agents, and no unnecessary abstraction.

🚀 What This Project Does

The system uses three Datapizza agents to automatically build:

a multi-phase roadmap for transitioning into AI/ML

a list of curated learning resources (with DuckDuckGo search)

a block-based weekly study plan with activities and mini-projects

No RAG. No vector DB. No pipelines hidden behind the curtain.
Just lightweight agents + explicit Python code.

🧩 Features

Datapizza Agents
Extremely simple agent definitions with clean prompts.

Web Search Integration
DuckDuckGo provides fresh, reliable learning resources.

Readable Sequential Pipeline
Three steps: roadmap → resources → study plan.

Ultra-Minimal Architecture
Inspired by the datapizza-buonanotte project:
clarity over complexity.

Portfolio-Friendly
Recruiters understand it at a glance.

📂 Project Structure
ai-learning-datapizza
│
├── main.py          # CLI entrypoint
├── config.py        # LLM + env config
├── agents.py        # Datapizza agents
├── tools.py         # Web search tool
├── pipeline.py      # Three-step pipeline
├── requirements.txt
└── .env.example

🔧 Installation
git clone https://github.com/lucalazzaro/ai-learning-datapizza
cd ai-learning-datapizza
pip install -r requirements.txt
cp .env.example .env


Edit .env with your API key.

▶️ Run
python main.py


You’ll be asked:

target role

your background

Then the pipeline will generate:

roadmap

resources

study plan

🏁 Why This Project Works

This is the perfect Level 2 project:

more advanced than no-code (Dify workflows)

lighter and cleaner than full RAG applications

demonstrates real multi-agent reasoning

easy to read, run, and extend

Datapizza AI keeps the code transparent, Python-first, and minimal.

📜 License

MIT License.