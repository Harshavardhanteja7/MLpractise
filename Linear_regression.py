import numpy as np
import pandas as pd
from sklearn import linear_model
from matplotlib import pyplot

overs = [1,2,3,4,5,6]
runs = [10,22,15,9,20,15]


x = np.array(overs).reshape(-1,1)
y = np.array(runs)

model = linear_model.LinearRegression()
model.fit(x, y)

pred_over = 3
pred_runs = model.predict([[pred_over]])

print(f"{pred_runs[0]:.2f}")

#Saved new changes