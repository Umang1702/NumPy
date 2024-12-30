import numpy as np  # Importing Numpy Library.

# Numpy Arrays Functions:-
# for 1d array:-
# search() function:-
variable= np.array([1,2,3,4,5,6,4,5,6,4])
# Indexing          0,1,2,3,4,5,6,7,8,9
search= np.where(variable==4)
print(search)
print("\n")
# searchsorted() function:-
searchsort= np.searchsorted(variable,5)
print(searchsort)
print("\n")
# sort() function:-
sort= np.sort(variable)
print(sort)
print("\n")

# sort() function for string array:-
string=np.array(["s","a","f","d"])
stringsort= np.sort(string)
print(stringsort)
print("\n")

# Filter the array in numpy:-
F=[True,False,True,False]
new_a=string[F]
print(new_a)
print("\n")


# sort() function for 2D array:-
d2=np.array([[3,2,1],[6,5,4]])
sort_2d=np.sort(d2)
print(sort_2d)