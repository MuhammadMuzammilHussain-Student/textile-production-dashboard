from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
import random
from datetime import datetime, timedelta
import json

app = FastAPI()
KIMI_API_KEY = os.environ.get("KIMI_API_KEY")

class MetricsResponse(BaseModel):
    modules: dict
    timestamp: str

class ModuleData(BaseModel):
    quality: dict
    production: dict
    inventory: dict
    planning: dict
    finance: dict
    marketing: dict

@app.get("/")
async def root():
    return FileResponse("index.html")

@app.get("/api/quality")
async def get_quality_metrics():
    return {
        "defect_rate": 2.1,
        "consistency": 96.4,
        "thread_break_rate": 0.8,
        "color_accuracy": 97.8,
        "trend": [2.5, 2.3, 2.2, 2.1, 2.0, 2.1, 2.1],
        "defects_by_type": {"color_variation": 35, "broken_thread": 28, "knots": 22, "fabric_density": 15},
        "prediction_next_7_days": {"predicted_defect_rate": 1.95, "confidence": 0.92},
        "root_causes": ["Temperature variance 2.3%", "Humidity fluctuation 1.8%", "Equipment calibration 0.9%"]
    }

@app.get("/api/production")
async def get_production_metrics():
    return {
        "capacity_utilization": 87.5,
        "production_speed": 1245,
        "units_produced": 5420,
        "equipment_status": {"loom_a": "operating", "loom_b": "operating", "loom_c": "maintenance"},
        "downtime_today": 45,
        "scheduled_vs_actual": {"scheduled": 5800, "actual": 5420, "variance": -7.2},
        "efficiency_trend": [85.2, 86.1, 86.8, 87.2, 87.5, 87.3, 87.5],
        "bottleneck_analysis": {"dyeing": 92, "weaving": 88, "finishing": 85},
        "next_30_days_forecast": {"predicted_capacity": 165000, "orders_booked": 152000, "buffer_capacity": 13000}
    }

@app.get("/api/inventory")
async def get_inventory_metrics():
    return {
        "raw_materials_status": {"cotton_yarn": {"stock": 450, "unit": "kg", "safety_level": 200, "reorder_point": 150}, "synthetic_yarn": {"stock": 320, "unit": "kg", "safety_level": 180, "reorder_point": 120}, "dyes": {"stock": 125, "unit": "L", "safety_level": 80, "reorder_point": 50}},
        "finished_goods": 4200,
        "work_in_progress": 850,
        "turnover_rate": 12.5,
        "stockout_risk": "medium_dyes",
        "demand_forecast_30days": {"expected_orders": 15800, "current_inventory": 4200, "gap": -11600},
        "inventory_optimization": {"carrying_cost_reduction": "18%", "improved_fulfillment": "94%"},
        "abc_analysis": {"high_value": 35, "medium_value": 42, "low_value": 23}
    }

@app.get("/api/planning")
async def get_planning_metrics():
    return {
        "schedule_adherence": 94.2,
        "active_orders": 48,
        "on_time_delivery_rate": 88.5,
        "resource_utilization": {"labor": 82, "machinery": 87, "materials": 75},
        "upcoming_orders": [{"order_id": "ORD-2025-001", "due_date": "2025-12-28", "status": "in_progress", "completion_pct": 65}, {"order_id": "ORD-2025-002", "due_date": "2025-12-30", "status": "queued", "completion_pct": 0}],
        "critical_path_items": ["Dye batch preparation", "Quality check setup"],
        "resource_bottlenecks": {"dyeing_line": "95%", "quality_team": "88%"},
        "predictive_delays": {"probability": "12%", "affected_orders": 5}
    }

@app.get("/api/finance")
async def get_finance_metrics():
    return {
        "revenue_mtd": 425000,
        "profit_margin": 18.5,
        "cost_per_unit": 12.50,
        "operating_expense_ratio": 24.3,
        "cash_flow": 125000,
        "revenue_trend": [380000, 390000, 410000, 415000, 420000, 425000],
        "cost_breakdown": {"raw_materials": 35, "labor": 22, "utilities": 15, "overhead": 18, "logistics": 10},
        "roi_by_product": {"premium_cotton": 22.5, "synthetic_blend": 18.3, "natural_fiber": 15.8},
        "budget_vs_actual": {"budget": 450000, "actual": 425000, "variance": -5.6},
        "predictive_revenue_q1": {"forecast": 1320000, "confidence": 0.88, "factors": ["seasonal_demand_up_12%", "new_client_acquisition"]}
    }

@app.get("/api/marketing")
async def get_marketing_metrics():
    return {
        "new_customers_mtd": 12,
        "customer_retention_rate": 91.5,
        "brand_awareness": 68,
        "market_share": 14.2,
        "sales_pipeline_value": 580000,
        "sales_by_segment": {"domestic": 62, "export": 38},
        "top_products": [{"name": "Premium Cotton", "revenue": 165000, "growth": "8.5%"}, {"name": "Synthetic Blend", "revenue": 142000, "growth": "5.2%"}],
        "customer_satisfaction": 4.6,
        "marketing_roi": 3.2,
        "lead_conversion_rate": 12.8,
        "demand_forecast_products": {"premium_cotton": "+15%", "synthetic_blend": "+8%", "natural_fiber": "-3%"}
    }

@app.get("/api/kpis")
async def get_kpis():
    return {
        "yield_pct": 94.2,
        "on_time_delivery": 88.5,
        "total_wastage": 5.8,
        "order_fill_rate": 91.2
    }

@app.get("/api/predictive-insights")
async def get_predictions():
    return {
        "prediction": "Quality metrics show excellent trend with 1.95% predicted defect rate. Production capacity at 87.5% utilization suggests room for 15% output increase without compromise. Inventory optimization indicates 18% potential cost reduction. Revenue forecast Q1: +12% YoY growth expected driven by seasonal demand and new client acquisition. Finance analysis shows strong margin sustainability at 18.5%.",
        "risk_level": "low",
        "modules_status": {"quality": "optimal", "production": "good", "inventory": "medium_risk", "planning": "on_track", "finance": "strong", "marketing": "positive_trend"}
    }

@app.get("/api/dashboard-summary")
async def get_dashboard_summary():
    quality = await get_quality_metrics()
    production = await get_production_metrics()
    inventory = await get_inventory_metrics()
    planning = await get_planning_metrics()
    finance = await get_finance_metrics()
    marketing = await get_marketing_metrics()
    
    return {
        "timestamp": datetime.now().isoformat(),
        "health_score": 8.4,
        "modules": {
            "quality": quality,
            "production": production,
            "inventory": inventory,
            "planning": planning,
            "finance": finance,
            "marketing": marketing
        }
    }

@app.get("/api/alerts")
async def get_alerts():
    return {
        "critical_alerts": 0,
        "warnings": 1,
        "info_messages": 3,
        "alerts": [
            {"type": "warning", "title": "Low Dye Stock", "message": "Dye inventory at 45% capacity. Recommend reorder within 48 hours.", "timestamp": "2025-12-23T18:42:00", "module": "inventory"},
            {"type": "info", "title": "Loom C Maintenance", "message": "Scheduled maintenance completed. Equipment ready for operation.", "timestamp": "2025-12-23T17:30:00", "module": "production"},
            {"type": "info", "title": "Order Fulfilled", "message": "Order #12345 ready for shipment. Revenue impact: +$8,500.", "timestamp": "2025-12-23T16:15:00", "module": "marketing"},
            {"type": "info", "title": "Quality Target Met", "message": "Defect rate below target (2.1% vs 2.5% threshold). Process performing optimally.", "timestamp": "2025-12-23T14:00:00", "module": "quality"}
        ]
    }
