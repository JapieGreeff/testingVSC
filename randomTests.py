import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


samples = 10000 
# creating a roughly uniform distribution with np.random
x = np.random.rand(samples)
plt.xlabel('time(s)')
plt.ylabel('value')
plt.plot(x)
plt.show()
plt.hist(x, bins = int(samples/10))
plt.show()

# adding each of the datapoints together of a number of uniform distributions gives you a gausian distribution
x = np.random.rand(samples)
numberOfDistributions = 10
for _ in range(0,numberOfDistributions):
    x = np.add(x,  np.random.rand(samples))
x = x/numberOfDistributions # normalise
plt.xlabel('time(s)')
plt.ylabel('value')
plt.plot(x)
plt.show()

plt.hist(x, bins = int(samples/10))
plt.show()

