import numpy as np
from pricing.elasticity_engine import EconometricPricingEngine

def run_pricing_analytics():
    print("=" * 64)
    print("   ECONOMETRIC PRICE ELASTICITY & REVENUE OPTIMIZATION ENGINE   ")
    print("=" * 64)

    # Synthetic realistic price & demand observation logs
    np.random.seed(42)
    sample_prices = np.array([45.0, 48.0, 50.0, 52.0, 55.0, 58.0, 60.0, 65.0, 70.0, 75.0])
    # True elasticity ~ -1.8
    true_elasticity = -1.8
    base_demand = 8000.0
    sample_demand = base_demand * ((sample_prices / 50.0) ** true_elasticity) * np.random.normal(1.0, 0.04, len(sample_prices))

    # 1. Log-Log Econometric Regression
    print("\n[1] Fitting Log-Log Econometric Demand Curve...")
    fit_res = EconometricPricingEngine.fit_log_log_elasticity(sample_prices, sample_demand)
    for k, v in fit_res.items():
        print(f"  --> {k}: {v}")

    # 2. Optimal Price Derivation
    marginal_cost = 22.50
    print(f"\n[2] Deriving Profit-Maximizing Price (Marginal Cost = ${marginal_cost:.2f})...")
    opt_res = EconometricPricingEngine.calculate_optimal_price(
        elasticity=fit_res["elasticity_coefficient"],
        marginal_cost=marginal_cost,
        intercept=fit_res["intercept"]
    )
    for k, v in opt_res.items():
        print(f"  --> {k}: {v}")

    print("\n" + "=" * 64)
    print("        DYNAMIC PRICING ANALYTICS COMPLETE (100%)               ")
    print("=" * 64)

if __name__ == "__main__":
    run_pricing_analytics()
