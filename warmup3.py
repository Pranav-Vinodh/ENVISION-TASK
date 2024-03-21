import numpy as np
array = np.array([[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12]])
row_norm_array = array/np.linalg.norm(array, axis =1,keepdims = True )
column_norm_array = array/np.linalg.norm(array,axis = 0,keepdims= True)

print("row-wise normalised: ")
print(row_norm_array)
print("\n")
print("column-wise normalised array: ")
print(column_norm_array)
