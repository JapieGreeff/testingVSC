import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# plotting XY/TZ
c1 = np.arange(0,10,1)
c2 = np.arange(1,11,1)
t1 = np.arange(0,10,1)
t2 = np.arange(10,20,1)
print(c1)
print(c2)
print(t1)
print(t2)
plt.plot(t1,c1,t2,c2)
plt.show()