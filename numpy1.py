#Basic math and shaping in numpy 
import numpy as np
salary = [10,37,22,8,12,14]

#We use numpy ot make mathematical operations easy
new_salary = np.array(salary)

#As we can multiple the contents of lists easily without iterating 
print(new_salary*1.4)

Bike_mileage = [35,45,50,53,20,27]
avg_mileage = np.array(Bike_mileage)

print(f"{sum(avg_mileage)/len(avg_mileage):.2f}")


#Python automatically calculates the row when we give -1 or gve exact value of 6 in this case as rows if other number it throws error
temp = [12,23,32,15,25,37]

x = np.array(temp).reshape(-1,1) #Default
# x = np.array(temp).reshape(5,1)  #Error
# x = np.array(temp).reshape(6,1)  #Correct
# You can give (1,-1) for rows and columns opposite if you need 1 rows and n columns just reverse

print(x)

#Numpy is Numeric python