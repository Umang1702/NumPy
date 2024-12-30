import numpy as np  # Improting Numpy Library.

# copy() Function:-
variable=np.array([1,2,3,4])
print("The original value of variable is:-",variable)
copy=np.copy(variable)
print("The Output of Copy() function:-",copy)
print("\n")

#view() Function:-
variable_1=np.array([1,2,3,4])
print("The original value of variable is:-",variable_1)
view=variable_1.view()
print("The Output of view() function:-",view)


#view() Function different to copy() function:-
variable_1=np.array([1,2,3,4])
print("The original value of variable is:-",variable_1)
print("The output of view() function before changing the value in variable:-",view)
view=variable_1.view()
variable_1[1]=30
print("The Output of view() function after changing the value in variable:-",view)