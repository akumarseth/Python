import numpy as np

a = np.arange(12).reshape((3,4))
print(a)

"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
"""

for row in a:
    print(row)

"""
[0 1 2 3]
[4 5 6 7]
[ 8  9 10 11]
"""

for row in a:
    for cell in row:
        print(cell)


"""
0
1
2
3
4
5
6
7
8
9
10
11
"""

for cell in a.flatten():
    print(cell)

"""
0
1
2
3
4
5
6
7
8
9
10
11
"""
print("*******************************")
for x in np.nditer(a, order='C'):
    print(x)

"""
0
1
2
3
4
5
6
7
8
9
10
11
"""

for x in np.nditer(a, order='F'):
    print(x)

"""
0
4
8
1
5
9
2
6
10
3
7
11
"""

for x in np.nditer(a, order='F', flags=['external_loop']):
    print(x)

"""
[0 4 8]
[1 5 9]
[ 2  6 10]
[ 3  7 11]
"""
print("*************************")
for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = x*x

print(a)

"""
[[  0   1   4   9]
 [ 16  25  36  49]
 [ 64  81 100 121]]
"""

b = np.arange(3,15,4).reshape(3,1)
print(b)

"""
[[ 3]
 [ 7]
 [11]]
"""

for x,y in np.nditer([a,b]):
    print(x,y)

"""
0 3
1 3
4 3
9 3
16 7
25 7
36 7
49 7
64 11
81 11
100 11
121 11
"""

b= np.arange(3,19,5).reshape(4,1)
print(b)

"""
[[ 3]
 [ 8]
 [13]
 [18]]
"""

for x,y in np.nditer([a,b]):
    print(x,y)

"""
for x,y in np.nditer([a,b]):
ValueError: operands could not be broadcast together with shapes (3,4) (4,1) 
"""