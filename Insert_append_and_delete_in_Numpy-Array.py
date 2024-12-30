import numpy as np # Importing Numpy libaray.

# insert() function in 1D:-
variable= np.array([1,2,3,4])
print(variable)
insert= np.insert(variable,(2,4),40) #(2,4) for multiple value
print("Output of insert() function for 1D array:",insert)
print("\n")

# insert() function in 2D:-
variable_1= np.array([[1,2,3,4],[5,6,7,8]])
print(variable_1)
insert_1D= np.insert(variable_1,2,6,axis=0) 
print("Output of insert() function for 2D array:",insert_1D)

# Define the 1D array
variable_3 = np.array([1, 2, 3, 4])
print("Original array:", variable_3)

# Append the element '1' to the end of the array
append = np.append(variable_3, 1)
print("Output of append() function for 1D array:", append)

# Define the 1D array
variable_2 = np.array([1, 2, 3, 4])
print("Original array:", variable_2)

# Delete the element at index 1
delete = np.delete(variable_2, 1)
print("Output of delete() function for 1D array:", delete)
