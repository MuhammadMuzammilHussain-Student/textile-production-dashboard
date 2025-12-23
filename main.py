# Textile Dashboard Backend with Kimi K2 AI
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os

app = FastAPI()

KIMI_API_KEY = os.environ.get("KIMI_API_KEY")

class KPIResponse(BaseModel):
    yield_pct: float
    on_time_delivery: float
    total_wastage: float
    order_fill_rate: float

class PredictionResponse(BaseModel):
    prediction: str
    risk_level: str

@app.get("/")
async def read_index():
    return FileResponse('index.html')

@app.get("/api/kpis", response_model=KPIResponse)
async def get_kpis():
    return {
        "yield_pct": 94.2,
        "on_time_delivery": 88.5,
        "total_wastage": 5.8,
        "order_fill_rate": 91.2
    }

@app.get("/api/predictive-insights", response_model=PredictionResponse)
async def get_prediction():
    # For now, return a demo prediction. In production, this would call Kimi API
    # Insights based on current textile production metrics
    insights = {
        "prediction": "Current yield at 94.2% is excellent. Wastage at 5.8% is within acceptable range. On-time delivery at 88.5% suggests good supply chain management. Recommend monitoring loom efficiency to maintain quality levels.",
        "risk_level": "Low"
    }
    return insights

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
