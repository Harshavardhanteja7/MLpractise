import numpy as np

players_earnings = [120000,145678, 123456, 234567, 6754321, 345621]

#Convert to np array

x = np.array(players_earnings)

print(np.min(x)) #Min of list

print(np.max(x)) #max of list

print(np.average(x)) #Avg of list

print(np.array(x[np.array(x)>200000])) #earnings > 2000000

print(np.array(x[np.array(x)>1]))