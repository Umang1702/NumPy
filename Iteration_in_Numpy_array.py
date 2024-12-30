import numpy as np  # Importing Numpy Library.
# Iteration of 1D Array:-
variable= np.array([1,2,3,4])
print("Iteration output of 1D array:")
for i in variable:
    print(i)
print("\n")

# Iteration of 2D Array:-
variable_1= np.array([[1,2,3,4],[5,6,7,8]])
print("Iteration output of 2D array:")
for i in variable_1:
    for j in i:
        print(j)
print("\n")

# Iteration of 3D Array:-
variable_2= np.array([[[1,2,3,4],[5,6,7,8],[11,12,13,14]]])
print("Iteration output of 3D array:")
for i in variable_2:
    print()
    for j in i:
        print()
        for k in j:
            print(k)