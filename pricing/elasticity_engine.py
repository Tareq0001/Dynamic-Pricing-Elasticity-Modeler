import numpy as np
import pandas as pd
from scipy import stats

class EconometricPricingEngine:
    @staticmethod
    def fit_log_log_elasticity(prices: np.ndarray, quantities: np.ndarray) -> dict:
        prices = np.asarray(prices, dtype=float)
        quantities = np.asarray(quantities, dtype=float)

        log_p = np.log(prices)
        log_q = np.log(quantities)

        # OLS regression: ln(Q) = alpha + beta * ln(P)
        slope, intercept, r_value, p_value, std_err = stats.linregress(log_p, log_q)
        elasticity = slope

        classification = "INELASTIC" if abs(elasticity) < 1.0 else "ELASTIC"

        return {
            "elasticity_coefficient": round(float(elasticity), 4),
            "classification": classification,
            "r_squared": round(float(r_value ** 2), 4),
            "p_value": round(float(p_value), 6),
            "intercept": round(float(intercept), 4)
        }

    @staticmethod
    def calculate_optimal_price(elasticity: float, marginal_cost: float, intercept: float) -> dict:
        if elasticity >= -1.0:
            return {"error": "Demand is inelastic or positive; unbounded theoretical revenue curve."}

        # Optimal price formula: P* = c * (e / (1 + e))
        optimal_price = marginal_cost * (elasticity / (1.0 + elasticity))
        optimal_quantity = np.exp(intercept) * (optimal_price ** elasticity)
        max_profit = (optimal_price - marginal_cost) * optimal_quantity

        return {
            "optimal_price": round(float(optimal_price), 2),
            "expected_quantity": round(float(optimal_quantity), 2),
            "expected_profit": round(float(max_profit), 2),
            "markup_percentage": round(float(((optimal_price - marginal_cost) / marginal_cost) * 100), 2)
        }
