# Dynamic-Pricing-Elasticity-Modeler 🏷️💹

An econometric analytics and revenue management MVP. Estimates log-log price elasticity of demand (PED), determines profit-maximizing price points, and runs demand simulation under competitive price shifts.

## Mathematical Implementations
1. **Log-Log Isoelastic Demand Formulation:**
   $$\ln(Q) = \beta_0 + \epsilon_p \ln(P) + \sum \gamma_i X_i$$
   Where $\epsilon_p = \frac{\% \Delta Q}{\% \Delta P}$ is the direct Price Elasticity Coefficient.
2. **Profit & Revenue Maximization:**
   $$\Pi(P) = (P - c) \cdot Q(P) = (P - c) \cdot e^{\beta_0} P^{\epsilon_p}$$
   Analytical optimal price under constant marginal cost $c$:
   $$P^* = c \cdot \left(\frac{\epsilon_p}{1 + \epsilon_p}\right) \quad \text{for } \epsilon_p < -1$$
