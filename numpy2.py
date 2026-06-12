#Indexing and slicing
import numpy as np
employee = np.array([["AL68568","HARSHA"],["AL68565","JULIE"],["AL68567","NICK"]])

print(employee[0]) #gets the first pair of 2D array
print(employee.shape) #This can be used to identify the shape in numpy array
print(employee[:,1]) #Here 1 represent the second element of inner list (you got this)

#task
customers = np.array([
 [1,2000],
 [2,3000],
 [3,5000]
])

print(f"Customers IDs are:{customers[:,0]}")
print(customers[:1])
print(customers.shape)

print(f"Customers IDs are:{customers[:,0]}")
print(f"Purchase amounts are:{customers[:,1]}")
print(customers[:1])
print(customers.shape)

#Statistics and in-built methods 

orders = np.array([
    [100],
    [200],
    [700],
    [1300],
    [123.5]
])

print(f"{np.max(orders):.0f}") #This is how you write not to get decimals vimp always inside formatted string only
print(np.min(orders))
print(np.average(orders))
print(np.sum(orders))


#Task to analysze my bike trip analysis
expenses = [500,600,400,700]
np_expenses = np.array(expenses) #Here we converted the normal list in 2D array for numpy operations
print(np_expenses.shape)
print(np.min(np_expenses))
print(np.sum(np_expenses))
print(f"Average is {np.average(np_expenses):.0f}")
print(np.flip(np_expenses)) #This is used to revrse/flip the contents in 2D array

#All the baove are basic requirements of numpy