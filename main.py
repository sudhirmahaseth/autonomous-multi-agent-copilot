import os
from fastapi import FastAPI, HTTPException, Header
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
async def trigger_research_workflow(request: ResearchRequest, x_api_key: str = Header(None)):
    # Pehle check karega ki environment me key hai ya nahi, 
    # agar nahi hai toh check karega ki user ne Header (X-API-Key) me bheji hai ya nahi.
    api_key = os.getenv("OPENAI_API_KEY") or x_api_key
    
    if not api_key:
        raise HTTPException(
            status_code=400, 
            detail="OpenAI API Key is missing. Please provide it in the 'X-API-Key' Header to test the endpoint."
        )
    
    try:
        # Mock execution response of LangGraph State Graph & CrewAI execution
        # Note: Jab aap actual workflow lagayein, toh llm initialize karte waqt 'openai_api_key=api_key' pass karein.
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
