# claims-frequency-simulation
This is a model that I have created, with the use of Poisson and Lognormal distributions, to analyse/model aggregate losses distributions

It is designed as a small, self-contained example of applying stochastic modelling in Python. 

Model:
Claim frequency N ~ Pois(λ)
Claim severity X ~ Lognormal (μ,σ)
Aggregate loss S = ∑X_i (from i = 1 to i = n)

In this example, it is assumed that lambda is 2, meaning that there is an average of 2 claims per year. The severity of the claim is modelled with a lognormal distribution where the mean is fixed at 8 and the standard deviation at 1. 

The model then runs 10000 (n_year) Poisson distribution tests, and see if the frequency of the claims is greater than 1. Then, if it is greater than 0, then run the lognormal distribution to insert the loss into the aggregate loss array, for the specific year. 

Finally, in the summary of the statistic, the mean, std, the mean of the aggregated loss and the 95 and 99 percentile of the aggregate loss is shown (95 for a one-in-20 bad years and 99 for a one-in-100 bad years)
