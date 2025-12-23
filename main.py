from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import pandas as pd
import os
import httpx

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
    if not KIMI_API_KEY:
        return {"prediction": "Kimi API key not configured.", "risk_level": "N/A"}
    
    current_metrics = "Yield: 94.2%, Wastage: 5.8%, OTD: 88.5%"
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.moonshot.cn/v1/chat/completions",
                headers={"Authorization": f"Bearer {KIMI_API_KEY}"},
                json={
                    "model": "moonshot-v1-8k",
                    "messages": [
                        {"role": "system", "content": "You are a textile production analyst. Analyze metrics and predict wastage risks. Keep it brief (under 50 words)."},
                        {"role": "user", "content": f"Analyze these metrics and predict next week's wastage: {current_metrics}"}
                    ],
                    "temperature": 0.3
                }
            )
            data = response.json()
            prediction = data['choices'][0]['message']['content']
            return {"prediction": prediction, "risk_level": "Medium"}
    except Exception as e:
        return {"prediction": f"Error calling Kimi API: {str(e)}", "risk_level": "Error"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
