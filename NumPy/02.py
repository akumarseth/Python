import numpy as np

a= np.array([5,6,9])
print(a[0]) # 5
print(a[1]) # 6
print(a.ndim) #1

a = np.array([[1,2],[3,2],[6,3]])
print(a.ndim) # 2
print(a.itemsize) # 4

print(type(a)) # <class 'numpy.ndarray'>
print(a.dtype) # int32

a = np.array([[1,2],[3,2],[6,3]], dtype=np.float64)
print(a.dtype) # float64
print(a.itemsize) # 8
print(a)

"""
print(a
[[1. 2.]
 [3. 2.]
 [6. 3.]]
"""

print(a.size) # 6
print((a.shape)) # (3, 2)

a = np.array([[1,2],[3,2],[6,3]], dtype=complex)
print(a)
"""
[[1.+0.j 2.+0.j]
 [3.+0.j 2.+0.j]
 [6.+0.j 3.+0.j]]
"""

print(np.zeros((3,4)))
"""
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
"""

print(np.ones((3,4)))
"""
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
"""

l = range(5)
print(l[0]) # 0
print(l[1]) # 1

print(np.arange(1,5)) # [1 2 3 4]

print(np.arange(1,6,2)) # [1, 3, 5]
print(np.arange(1,5,2)) # [1, 3]

print(np.linspace(1,5,10))

"""
[1.         1.44444444 1.88888889 2.33333333 2.77777778 3.22222222
 3.66666667 4.11111111 4.55555556 5.        ]
"""

print(np.linspace(1,5,20))

"""
[1.         1.21052632 1.42105263 1.63157895 1.84210526 2.05263158
 2.26315789 2.47368421 2.68421053 2.89473684 3.10526316 3.31578947
 3.52631579 3.73684211 3.94736842 4.15789474 4.36842105 4.57894737
 4.78947368 5.        ]
"""

a = np.array([[1,2],[3,4],[5,6]])
print(a)

"""
[[1 2]
 [3 4]
 [5 6]]
"""

print(a.shape) #(3, 2)

print(a.reshape(2,3))
"""
[[1 2 3]
 [4 5 6]]
"""
print(a.reshape(6,1))
"""
[[1]
 [2]
 [3]
 [4]
 [5]
 [6]]
"""

print(a.ravel()) # [1 2 3 4 5 6]

print(a.min()) # 1
print(a.max()) # 6
print(a.sum()) # 21
print(a.sum(axis=0)) # [ 9 12]
print(a.sum(axis=1)) # [ 3  7 11]

print(np.sqrt(a))

"""

[[1.         1.41421356]
 [1.73205081 2.        ]
 [2.23606798 2.44948974]]
"""

print(a)

"""
[[1 2]
 [3 4]
 [5 6]]
"""

print(np.std(a)) # 1.707825127659933

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(a)

"""
[[1 2]
 [3 4]]
"""
print(b)

"""
[[5 6]
 [7 8]]
"""

print(a+b)

"""
[[ 6  8]
 [10 12]]
"""

print(a-b)
"""
[[-4 -4]
 [-4 -4]]
"""
print(a*b)

"""
[[ 5 12]
 [21 32]]
"""

print(a/b)

"""
    [[0.2        0.33333333]
 [0.42857143 0.5       ]]
"""

print(a.dot(b))

"""
[[19 22]
 [43 50]]
"""