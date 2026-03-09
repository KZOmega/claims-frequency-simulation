import numpy as np
import pandas as pd

#1. Set up the parameters
n_years = 10000
lam = 2.0 #representing that there are 2 claims each year
mu = 8.0 #lognormal claims severity mean
sigma = 1.0 #lognormal claims severity s.d.
rng=np.random.default_rng(42) #random number generator which is reproducable (seed 42)

#2. Simulate claim frequency for each year
n_claims = rng.poisson(lam=lam, size=n_years)
print(n_claims)
#3. Simulate severities and aggregate losses per year
aggregate_losses = np.zeros(n_years)
print(aggregate_losses)
for i in range(n_years):
    if n_claims[i] > 0:
        severities = rng.lognormal(mean=mu, sigma=sigma, size=n_claims[i])
        aggregate_losses[i]=severities.sum()
    # if 0 claims, aggregate loss stays 0

# 4. Basic summary statistics
results = {
    "mean_aggregate_loss": aggregate_losses.mean(),
    "std_aggregate_loss": aggregate_losses.std(),
    "prob_loss_zero": np.mean(aggregate_losses == 0),
    "p95_aggregate_loss": np.percentile(aggregate_losses, 95),
    "p99_aggregate_loss": np.percentile(aggregate_losses, 99),
}
#Print results without properly formatting it
print(results)
