import numpy as np

print('numpy:',np.__version__)

#print(dir(np))


## np.array()
## tolist()
## shape
## dtype -> str, int, float, bool, list, None
## type(..)
## reshape()
## flattened()
## 


print("\n")
print("\n")
print("\n")
print("\n")


python_list = [1,2,3,4,5]

print('Type',type (python_list))

print(python_list)

two_D_List = [[0,1,2],[3,4,5],[6,7,8],[9,10,11]]

print(two_D_List)


np_array_from_list = np.array(python_list)

print(type(np_array_from_list))
print(np_array_from_list)


np_array_from_list = np.array(two_D_List)
print(np_array_from_list)


print("reshape: " , np_array_from_list.reshape(3,4))

np_array_from_list2 = np.array(python_list, dtype=float)
print(np_array_from_list2)



nmpy_bool_list = np.array([0,1,-1,-2,0,1,0,0], dtype=bool)
print(nmpy_bool_list)




np_array_from_tuple = np.array((1,2,3,4,5))
print(type(np_array_from_tuple))

print(np_array_from_tuple)

print(np_array_from_list.shape)


print(np_array_from_list.size)
print(np_array_from_list.base)
print(np_array_from_list.__class__)



## Mathematical operations

numpy_array_from_list = np.array([1, 2, 3, 4, 5,20])

print(numpy_array_from_list + 10)

print(numpy_array_from_list - 10)

print(numpy_array_from_list * 10)

print(numpy_array_from_list / 10)

print(numpy_array_from_list % 2)

print(numpy_array_from_list // 10)

print(numpy_array_from_list ** 2)



## horizontal stack

np_list_one = np.array([1,2,3])

np_list_two = np.array([4,5,6])


print(np_list_one + np_list_two)

print(np.hstack((np_list_one, np_list_two)))
print(np.vstack((np_list_one, np_list_two)))



## Random numbers

random_float = np.random.random()
print(random_float)

random_float = np.random.random(5)
print(random_float)

random_int = np.random.randint(5, 15, size=5)
print(random_int)