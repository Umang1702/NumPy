import numpy as np  # Importing Numpy Library.

# Shape() function in Numpy array:-
variable= np.array([[1,2,3],[4,5,6]])
shape= np.shape(variable)  # Use of shaoe() Function in Numpy.
reshape=variable.reshape(2,3) # 2 -->Row and 3 --> Column
print("The output of the shape() function in Numpy array is:",shape)
print("The output of the reshape() function in Numpy array is:",reshape)