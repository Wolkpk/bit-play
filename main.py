import scipy.stats as stats
prob = 1- stats.binom.cdf(6, 10, 0.5)
print("the probablity of getting more than 6 head in 10 coin flip is:", round(prob,3))