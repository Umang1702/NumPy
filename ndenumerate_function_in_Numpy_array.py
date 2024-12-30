import numpy as np  # Importing Numpy Library.
# Use of ndenumerate() function in Numpy array for iteration:-
variable_3 = np.array([[[1,2,3,4],[5,6,7,8]]])
print("The dimension of the array is:",variable_3.ndim) # Use to find the dimension of the array.
for i,d in np.ndenumerate(variable_3): # Use of nditer() function.
    print(i,d)