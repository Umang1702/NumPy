import numpy as np  # Importing the numpy library
# 1-Dimensional Array:-
arr1=np.array([1,2,3,4,5])
print("Output of 1D array is: \n",arr1)
print("Type 1D array:",type(arr1))
print("\n")

# 2-Dimensional Array:-
arr2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("Output of 2D array is: \n",arr2)
print("Type of 2D array:",type(arr2))
print("\n")


# 3-Dimensional Array:-
arr3=np.array([[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]])
print("Output of 3D array is: \n",arr3)
print("Type of 3D array:",type(arr3))
print("\n")


# Higher-Dimensional Array:-
arr10=np.array([1,2,3,4],ndmin=10)
print("Output of 10D array is: \n",arr10)
print("Type of 10D array:",type(arr10))
