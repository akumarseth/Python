import numpy as np

n = [6,7,8]
print(n[0:2]) # [6,7]
print((n[-1])) # 8

a = np.array([6,7,8])
print(a[0:2]) # [6 7]
print(a[-1]) # 8

a = np.array([[6,7,8],[1,2,3],[9,3,2]])
print(a)

"""
[[6 7 8]
 [1 2 3]
 [9 3 2]]
"""

print(a[1,2]) # 3 # 1 is row and 2 is column

print(a[0:2,2]) # [8,3] # from 0 and 1 row it will print 2nd element

print((a-1)) # [9,3,2]

print(a[-1,0:2]) # [9, 3] # from the column 0 and 1 element

print(a[:,1:3])
"""
[[7 8]
 [2 3]
 [3 2]]
"""


for row in a:
    print(row)

"""
[6 7 8]
[1 2 3]
[9 3 2]
"""

for cell in a.flat:
    print((cell))
"""
6
7
8
1
2
3
9
3
2
"""

a=np.arange(6).reshape(3,2)
b=np.arange(6,12).reshape(3,2)
print(a)
"""
[[0 1]
 [2 3]
 [4 5]]
"""
print(b)
"""
[[ 6  7]
 [ 8  9]
 [10 11]]
"""

print(np.vstack((a,b)))
"""
[[ 0  1]
 [ 2  3]
 [ 4  5]
 [ 6  7]
 [ 8  9]
 [10 11]]
"""
print(np.hstack((a,b)))
"""
[[ 0  1  6  7]
 [ 2  3  8  9]
 [ 4  5 10 11]]
"""

a=np.arange(30).reshape(2,15)
print(a)

"""
[[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
 [15 16 17 18 19 20 21 22 23 24 25 26 27 28 29]]
"""

print(np.hsplit(a,3))

"""
[array([[ 0,  1,  2,  3,  4],
       [15, 16, 17, 18, 19]]), array([[ 5,  6,  7,  8,  9],
       [20, 21, 22, 23, 24]]), array([[10, 11, 12, 13, 14],
       [25, 26, 27, 28, 29]])]
"""

result = np.hsplit(a,3)
print(result[0])
"""
[[ 0  1  2  3  4]
 [15 16 17 18 19]]
"""
print(result[1])
"""
[[ 5  6  7  8  9]
 [20 21 22 23 24]]
"""

print(result[2])
"""
[[10 11 12 13 14]
 [25 26 27 28 29]]
"""

print(np.vsplit(a,2))
"""
[array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14]]), 
array([[15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])]
"""

result = np.vsplit(a,2)
print(result[0])
"""
[[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]]
"""
print(result[1])
"""
[[15 16 17 18 19 20 21 22 23 24 25 26 27 28 29]]
"""

a= np.arange(12).reshape(3,4)
print(a)
"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
"""

print(a > 4)
"""
[[False False False False]
 [False  True  True  True]
 [ True  True  True  True]]
"""

b= a > 4
print(a[b]) # [ 5  6  7  8  9 10 11]

a[b]=-1
print(a)

"""
[[ 0  1  2  3]
 [ 4 -1 -1 -1]
 [-1 -1 -1 -1]]
"""