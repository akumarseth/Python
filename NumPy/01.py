import numpy as np
import time
import sys

l = range(10000)
print(sys.getsizeof(5)*len(l))

array = np.arange(1000)
print(array.size * array.itemsize)

SIZE  =100000

l1 = range(SIZE)
l2= range(SIZE)

a1 = np.array(SIZE)
a2=np.array(SIZE)

#Python list

start = time.time()
result = [(x+y) for x,y in zip(l1, l2)]
print("Python list took: ", (time.time()-start)*1000)

start = time.time()
result = a1+a2
print("NumPy took:", (time.time()-start)*1000)

