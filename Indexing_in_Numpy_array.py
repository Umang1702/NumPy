import numpy as np
# Indexing for 1 D NumPy array:-
variable = np.array([1,2,3,4])
# Indexing          0,1,2,3
print("The dimension of the array is: ",variable.ndim)  # Use to ceheck the dimension of the array.
print("Output for Indexing of the 1D Array:",variable[1])  # indexing 1 = 2 .
print("\n")

# Negative Indexing for 1 D NumPy array:-
variable = np.array([1,2,3,4])
# Indexing          -4,-3,-2,-1
print("The dimension of the array is: ",variable.ndim)  # Use to ceheck the dimension of the array.
print("Output for Negative Indexing of the 1D Array:",variable[-2])  # indexing 1 = 2 .
print("\n")

# For 2D aaray
#Indexing for 2D array :- 0     1
variable_2 =  np.array([[1,2],[3,4]])
# Indexing for elements:-0,1   0,1
print("The dimension of the array is: ",variable_2.ndim)  # Use to ceheck the dimension of the array.
print("Output for Indexing of the 2D Array:",variable_2[1,1])


# For 3D aaray
#Indexing for 3D array :- 0     1     2
variable_3 =  np.array([[[1,2],[5,6],[3,4]]])
# Indexing for elements:-0,1   0,1   0,1
print("The dimension of the array is: ",variable_3.ndim)  # Use to ceheck the dimension of the array.
print("Output for Indexing of the 2D Array:",variable_3[0,2,1])