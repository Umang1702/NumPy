import numpy as np  # Importing Numpy Library.
# Matrix Functions:-
# transpose() function:-
variable = np.matrix([[1,2,3],[5,6,7]])
print("The Orignal array:-\n",variable)
print("\n")
print("The output of transpose() function is:-\n",np.transpose(variable))
print("\n")


# swapaxes() function:-
variable1 = np.matrix([[1,2,3],[5,6,7]])
print("The Orignal array:-\n",variable1)
print("\n")
print("The output of swapaxes() function is:-\n",np.swapaxes(variable1,0,1))
print("\n")


# linalg.inv() function:-
variable2 = np.matrix([[1,2],[5,6]])
print("The Orignal array:-\n",variable2)
print("\n")
print("The output of linalg.inv() function is:-\n",np.linalg.inv(variable2))
print("\n")


# linalg.matrix_power() function:-
variable3 = np.matrix([[1,2],[5,6]])
print("The Orignal array:-\n",variable3)
print("\n")
print("The output of linalg.matrix_power() function is:-\n",np.linalg.matrix_power(variable3,0))
print("\n")


# linalg.det() function:-
variable4 = np.matrix([[1,2,3],[3,4,3],[1,2,3]])
print("The Orignal array:-\n",variable4)
print("\n")
print("The output of linalg.det() function is:-\n",np.linalg.det(variable4))