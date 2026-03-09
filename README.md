# claims-frequency-simulation
This is a model that I have created, with the use of Poisson and Lognormal distributions, to analyse/model aggregate losses distributions

It is designed as a small, self-contained example of applying stochastic modelling in Python. 

Model:
Claim frequency N ~ Pois(λ)
Claim severity X ~ Lognormal (μ,σ)
Aggregate loss S = ∑X_i (from i = 1 to i = n)

In the base case, the model simulates 10,000 policy‑years, with an expected 2 claims per year and right‑skewed claim sizes.
