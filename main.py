import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Autonomous Multi-Agent Copilot API",
    description="FastAPI backend running LangGraph and CrewAI Multi-Agent research workflow.",
    version="1.0.0"
)

class ResearchRequest(BaseModel):
    topic: str
    depth: str = "comprehensive"

@app.get("/")
async def root():
    return {"status": "online", "message": "Multi-Agent Copilot is running"}

@app.post("/api/v1/research")
async def trigger_research_workflow(request: ResearchRequest):
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(status_code=500, detail="OpenAI API Key is missing in environment configuration.")
    
    try:
        # Mock execution response of LangGraph State Graph & CrewAI execution
        # In production, this triggers your graph compiled workflow: app = workflow.compile()
        return {
            "status": "success",
            "topic": request.topic,
            "metrics": {
                "time_saved_estimated": "50%",
                "status_code": "COMPLETED"
            },
            "payload": {
                "summary": f"Synthesized research report data regarding: {request.topic}.",
                "agents_involved": ["Research Analyst Agent", "Data Synthesizer Agent"],
                "orchestrator": "LangGraph Stateful Router"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
