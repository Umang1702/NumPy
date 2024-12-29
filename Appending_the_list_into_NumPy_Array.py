import numpy as np  #Importing numpy library
# Create Empty list:-
list=[]
for i in range(1,7):
    element=int(input("Enter your element to insert:"))
    list.append(element)  # Insert elements into list.
arr=np.array(list) # Append the list into Array
print("Final Output in the form of array:",arr)
print("Type of the array is:",type(arr))