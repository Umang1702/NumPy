import numpy as np  # Importing Numpy Library
import random # Import Random Module

# Use of rand() function of Random module:-
variable=np.random.rand(4)  # Use The rand() function of the Random module.
print("Output of rand() function:\n",variable)
print("\n")

variable1=np.random.rand(2,3)  # 2 -> Row and 3 -> Column
print("Output of rand() function with column and rows values:\n",variable1)
print("\n")

# Use of randn() function of Random module:-
variable2=np.random.randn(5)  # Use The randn() function of the Random module.
print("Output of randn() function:\n",variable2)
print("\n")
# The output of the randn() function gives the value opr elements which is close to zero.

# Use of randf() function of Random module:-
variable3=np.random.ranf(5)  # Use The randf() function of the Random module.
print("Output of ranf() function:\n",variable3)
print("\n")
# The output of the randn() function gives the Floating value or Floating elements .


# Use of randint() function of Random module:-
variable4=np.random.randint(1,20,10)  # Use The randf() function of the Random module.
print("Output of randint() function:\n",variable4)
print("\n")
# The output of the randint() function gives the integer value or element between the given range as a parameter.