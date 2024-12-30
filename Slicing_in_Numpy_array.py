import numpy as np # Importing Numpy Library.

# Slicing of 1D array:-
variable= np.array([1,2,3,4])
slicing= variable[1:3] # value between index 1 to index (n-1) means 3-1=2
print("The dimension of the array is:",variable.ndim) # Use to check the dimensions of the array.
print(slicing)


# Slicing of 2D array:-
variable_1= np.array([[1,2,3,4],[5,6,7,8]])
slicing_1= variable_1[1,1:3] # 2nd array index is 1 and value between 1 to 3-1=2 of 2nd array
print("The dimension of the array is:",variable_1.ndim) # Use to check the dimensions of the array.
print(slicing_1)


# Slicing of 3D array:-
variable_3= np.array([[[1,2,3,4],[5,6,7,8],[11,12,13,14]]])
slicing_2= variable_3[0,1,1:3] 
print("The dimension of the array is:",variable_3.ndim) # Use to check the dimensions of the array.
print(slicing_2)