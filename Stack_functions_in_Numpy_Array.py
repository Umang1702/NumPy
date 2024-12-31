import numpy as np  # Importing Numpy Library.
# Stack Function:-
# stack() function for axis=1 and axis=0:-
var= np.array([1,2,3,4])
var1= np.array([9,8,7,6])
new_a1=np.stack((var,var1),axis=1)# Use of stack() function.
new_a0=np.stack((var,var1),axis=0)# Use of stack() function.
print("output of stack() function for axis=1:-\n",new_a1)
print("output of stack() function for axis=0:-\n",new_a0)
print("\n")


# hstack() function :-
var2= np.array([1,2,3,4])
var3= np.array([9,8,7,6])
new_a2=np.hstack((var2,var3))# Use of hstack() function for arranging array in row format.
print("output of hstack() function:-\n",new_a2)
print("\n")


# vstack() function :-
var4= np.array([1,2,3,4])
var5= np.array([9,8,7,6])
new_a3=np.vstack((var4,var5))# Use of vstack() function for arranging array in column format.
print("output of vstack() function:-\n",new_a3)
print("\n")


# dstack() function :-
var6= np.array([1,2,3,4])
var7= np.array([9,8,7,6])
new_a4=np.dstack((var6,var7))# Use of dstack() function for arranging array in height format.
print("output of dstack() function:-\n",new_a4)
print("\n")