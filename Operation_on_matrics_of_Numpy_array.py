import numpy as np  # Importing Numpy library.
# Addition of two matrix:-
var1=np.matrix([[1,2],[3,4]])
var2=np.matrix([[5,6],[7,8]])
addition=(var1+var2)
print("The output of addition:-\n",addition)
print("\n")



# Subtraction of two matrix:-
var3=np.matrix([[1,2],[3,4]])
var4=np.matrix([[5,6],[7,8]])
subtraction=(var3-var4)
print("The output of the subtraction is:-\n",subtraction)
print("\n")



# Multiply of two matrix:-
var5=np.matrix([[1,2],[3,4]])
var6=np.matrix([[5,6],[7,8]])
multiply=(var5*var6)
dotfun=np.dot(var5,var6)
print("Multiplying both matrix:-\n",multiply)
print("\n")
print("The output of dot() fun is:-\n",dotfun)
print("\n")
