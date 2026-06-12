#We will understand reshaping

import numpy as np

dataset_a = [30,40,23,34,56,13]

x = np.array(dataset_a).reshape(3,2) 
#Here above 3 is rows, and 2 is colums you can reshape data anyway you want -1 takes the len of list
print(x)

y = np.array(dataset_a).reshape(-1,2)
#Above reshape and this reshape is same as we gave -1, it actually checks the colums value 2 and fits the data into 2 cols and remaing rows
print(y)

Customer_Name = ['Harsha',123,'Karthik',124,'Karthik',125]

c = np.array(Customer_Name).reshape(-1,2)
print(c)
# Array alwasy takes one argument as input

#We have matrix multiplifactons in numpy

a_ex = np.array([[10],[12],[30]])
b_ex = np.array([10])
print(a_ex.dot(b_ex)) #This method multiplies a_ex with b_ex and results new array

# Matrices are mathematics functions