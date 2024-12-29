import numpy as np  # Importing the Numpy library

# Converting (int64) into (int32)
#The datatype of numpy array Before converting into another datatype.
before1=np.array([1,2,3,4])  #create new numpy array
print("Original array:",before1)
print("Before :",before1.dtype)
#The datatype of numpy array After converting into another datatype.
after1=np.array([1,2,3,4],dtype=np.int32)
print("Array after coverting into the (int32) datatype:",after1)
print("Datatype of (int32):",after1.dtype)
print("\n")

# Converting (int64) into (float)
#The datatype of numpy array Before converting into another datatype.
before2=np.array([1,2,3,4])  #create new numpy array
print("Original array:",before2)
print("Before :",before2.dtype)
#The datatype of numpy array After converting into another datatype.
after2=np.array([1,2,3,4],dtype="f")
print("Array after coverting into the (float) datatype:",after2)
print("Datatype of (float):",after2.dtype)
print("\n")


# Converting (int64) into (float32) by using float() function:-
#The datatype of numpy array Before converting into another datatype.
before3=np.array([1,2,3,4])  #create new numpy array
print("Original array:",before3)
print("Before :",before3.dtype)
#The datatype of numpy array After converting into another datatype.
after3=np.float32(before3)
print("Array after coverting into the (float32) datatype:",after3)
print("Datatype of (float32):",after3.dtype)
print("\n")


# Converting (int64) into (float) by using astype() function:-
#The datatype of numpy array Before converting into another datatype.
before4=np.array([1,2,3,4])  #create new numpy array
print("Original array:",before4)
print("Before :",before4.dtype)
#The datatype of numpy array After converting into another datatype.
after4=before4.astype(float)
print("Array after coverting into the (float64) datatype:",after4)
print("Datatype of (float64):",after4.dtype)
