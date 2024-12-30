import numpy as np # Importing Numpy Libaray.
import random  # Importing random module

#shuffle() function in NumPy:-
variable = np.array([1,2,3,4,5])
np.random.shuffle(variable) # everytime the value or the elements of the array will be new not same for evertime.
print("Output of shuffle() function:-",variable)
print("\n")

#unique() function in NumPy:-
variable_1 = np.array([1,2,3,4,5,76,5,43,4,5])
unique=np.unique(variable) # repeated element is not supported by unique() function.
print("Output of unique() function:-",unique)
print("\n")

#resize() function in NumPy:-
variable_2 = np.array([1,2,3,4,5,6,7,8])
resize=np.resize(variable_2,(4,2)) # resize the dimension of the array by using resize() function.
print("Output of resize() function:-",resize)
print("\n")

#flatten() and ravel() function in NumPy:-
variable_3 = np.array([1,2,3,4,5,6])
f=np.resize(variable_3,(3,2))
flatten=f.flatten(order="F") # Use of flatten() function.
print("Flatten() output:-",flatten)
ravel=np.ravel(f,order="K") # Use of ravel() function.
print("Ravel() output:-",ravel)