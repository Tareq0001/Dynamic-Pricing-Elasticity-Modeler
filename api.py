from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from pricing.elasticity_engine import EconometricPricingEngine

app = FastAPI(title="Dynamic Pricing & Elasticity Engine API", version="1.0.0")

class ElasticityRequest(BaseModel):
    prices: List[float]
    quantities: List[float]
    marginal_cost: float

@app.get("/")
def root():
    return {"service": "Econometric Pricing Analytics", "status": "ONLINE"}

@app.post("/pricing/optimize")
def optimize_pricing(req: ElasticityRequest):
    fit = EconometricPricingEngine.fit_log_log_elasticity(req.prices, req.quantities)
    if "elasticity_coefficient" in fit:
        opt = EconometricPricingEngine.calculate_optimal_price(fit["elasticity_coefficient"], req.marginal_cost, fit["intercept"])
        return {"elasticity_fit": fit, "revenue_optimization": opt}
    return fit
