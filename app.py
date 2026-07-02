from fastapi import FastAPI
from agents import run_agent

app = FastAPI()

@app.post("/review")
async def review(payload: dict):

    code = payload["code"]

    security = run_agent(
        "Security Reviewer",
        code
    )

    performance = run_agent(
        "Performance Reviewer",
        code
    )

    architecture = run_agent(
        "Architecture Reviewer",
        code
    )

    return {
        "security": security,
        "performance": performance,
        "architecture": architecture
    }