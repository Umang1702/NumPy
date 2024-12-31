import numpy as np  # Importing Numpy library.
# split() function for 1D array:-
variable= np.array([1,2,3,4,5,6])
split= np.array_split(variable,3)# Use of split() function.
print("Output of the split() function for 1D array:-\n",split)
print("\n")


# split() function for 2D array:-
variable= np.array([[1,2],[3,4],[5,6]])
split= np.array_split(variable,3)# Use of split() function.
print("Output of the split() function for 2D array:-\n",split)