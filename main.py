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

@app.get("/api/inventory")
async def get_inventory():
    """Returns current inventory status across all materials"""
    return {
        "raw_material_stock": 85.3,
        "finished_goods": 42.7,
        "work_in_progress": 23.5,
        "warehouse_utilization": 78.2,
        "material_categories": [
            {"name": "Cotton Yarn", "stock": 450, "unit": "kg", "status": "Sufficient"},
            {"name": "Synthetic Yarn", "stock": 320, "unit": "kg", "status": "Sufficient"},
            {"name": "Dyes", "stock": 125, "unit": "L", "status": "Low"},
            {"name": "Finishing Chemicals", "stock": 87, "unit": "L", "status": "Sufficient"}
        ]
    }

@app.get("/api/alerts")
async def get_alerts():
    """Returns system alerts and notifications"""
    return {
        "critical_alerts": 0,
        "warnings": 1,
        "info_messages": 3,
        "alerts": [
            {"type": "warning", "title": "Low Dye Stock", "message": "Dye inventory at 45% capacity", "timestamp": "2025-12-23T18:42:00"},
            {"type": "info", "title": "Loom C Maintenance", "message": "Scheduled maintenance completed", "timestamp": "2025-12-23T17:30:00"},
            {"type": "info", "title": "Order Fulfilled", "message": "Order #12345 ready for shipment", "timestamp": "2025-12-23T16:15:00"}
        ]
    }

@app.get("/api/performance")
async def get_performance():
    """Returns detailed performance metrics"""
    return {
        "overall_efficiency": 91.7,
        "production_capacity_utilization": 85.4,
        "equipment_health": 94.2,
        "labor_productivity": 88.6,
        "daily_targets": {
            "units_produced": 2450,
            "units_target": 2500,
            "achievement": 98.0
        },
        "kpi_trends": {
            "yield_trend": "+1.2%",
            "otd_trend": "-0.3%",
            "wastage_trend": "-0.5%",
            "efficiency_trend": "+0.8%"
        }
    }

@app.get("/api/export/report")
async def export_report():
    """Returns data for PDF/CSV export"""
    return {
        "report_title": "Textile Production Daily Report",
        "report_date": "2025-12-23",
        "period": "Daily",
        "summary": {
            "kpis": {"yield": 94.2, "otd": 88.5, "wastage": 5.8, "fill_rate": 91.2},
            "production": {"units_produced": 2450, "target": 2500},
            "quality": {"defect_rate": 2.1, "consistency": 96.4}
        },
        "export_available_formats": ["PDF", "CSV", "XLSX"]
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
