from numpy import *
'''
Monte Carlo valuation of European call option
in Black-Scholes-Merton model
'''

# Parameter values
S0 = 100     # initial index level
K = 105.     # strike price
T = 1.0      # tiime-to-maturity
r = 0.05     # riskless short rate
sigma = 0.2  # volatility

I = 100000   # number of simulations

# Valuation Algorithm
z = random.standard_normal(I)  # pseudorandom numbers
ST = S0 * exp((r - 0.5 * sigma ** 2) * T + sqrt(T) * 2)

# index values at maturity
hT = maximum(ST - K, 0)  # inner values at maturity
C0 = exp(-r * T) * sum(hT) / I  # Monte Carlo estimator

# Result output
print('The value of the European call option {}'.format(C0))
