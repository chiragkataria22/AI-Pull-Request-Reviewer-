Developers spend significant time reviewing pull requests.

Can multiple AI agents automate the first review pass?

Architecture

GitHub PR
    |
    v
Research Agent
    |
    +----> Code Review Agent
    |
    +----> Security Agent
    |
    +----> Performance Agent
    |
    v
Summary Agent
    |
    v
Review Report

Tech Stack

* Python
* OpenAI SDK
* FastAPI
* GitHub API
* LangGraph