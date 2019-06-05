import numpy as np

#generate a die with values 1 - n and fair distribution
def GetDNOne(n):
    values = np.arange(n) + 1
    probabilities = np.ones((n,), dtype=int) # assuming fair dice
    return np.column_stack((values, probabilities))

#generate a die with values 1 - n and fair distribution
def GetDN(n):
    values = np.arange(n) + 1
    probabilities = np.ones((n,), dtype=int) # assuming fair dice
    return np.column_stack((values, probabilities))


#generate values and probability set for n number of similar dice
def GetDiceSet(n, dice):
    if (n > 2):
        probability = np.convolve(dice[:,1], GetDiceSet(n-1, dice)[:,1])
    else:
        probability = np.convolve(dice[:, 1], dice[:, 1])
    value = np.arange((len(dice[:,1])*n-n+1)) + n
    return np.column_stack((value,probability))

#probdis = GetDiceSet(5, GetDN(20))
#print(probdis)
#sumTo1 = probdis[:,1]/np.sum(probdis[:,1])
#for x,y in zip(probdis[:,0], sumTo1):
#    print(x,y)

D6 = GetDN(6)
print(D6)