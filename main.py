from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import pandas as pd
import os

app = FastAPI()

class KPIResponse(BaseModel):
    yield_pct: float
    on_time_delivery: float
    total_wastage: float
    order_fill_rate: float

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

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
