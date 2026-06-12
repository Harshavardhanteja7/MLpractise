#Multiple Linear Regresion 

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#Train Data
overs = [18,10,12,6,20]
wickets = [5,2,1,0,3]
economy = [8,10.43, 9, 4, 10.1]

#Result data
rating = [8,7,6,5,3]

#training model
x = np.array([overs,wickets,economy]).T #Transpose is very imp as we have 3 imput factors
y = np.array(rating)


model = LinearRegression()
model.fit(x,y)

print(x.shape)

#Example to check normal list in np array to see shape you need to convert into np array to check shape
print(np.array(wickets).shape) 

predict_values = [12,4,10]
predict_rating = model.predict([predict_values])
# print(f"{predict_rating:.2f}")
print(f"{predict_rating[0]:.1f}")

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("R² score:", model.score(x, y))


#visualize
# plt.scatter(overs, rating, color = 'blue')
# plt.scatter(overs, predict_rating, color = 'red')

new_prediction = model.predict(x)
plt.scatter(overs, wickets, color='blue' , label='Actual data')
plt.scatter(overs, new_prediction, color='red',  label='Prediction data')
plt.xlabel("Overs")
plt.ylabel("Wickets")
plt.show()