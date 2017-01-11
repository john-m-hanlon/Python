import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

X = np.random.normal(0,1,100)
X2 = np.random.normal(0,1,100)

plt.plot(X)
plt.plot(X2)
plt.xlabel('Time')
plt.ylabel('Returns')
plt.legend(['X1, X2'])
plt.show()

print(np.mean(X))
print(np.std(X))

prices = open('DIS.txt','r').read()
#data = prices.read()
#print(prices)
#print(data)
openPrice = prices[1]
print(openPrice)
