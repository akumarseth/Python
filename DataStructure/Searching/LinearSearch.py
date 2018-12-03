# Python code for linearly search x in arr[].  If x
# is present then return its  location,  otherwise
# return -1
#The time complexity of above algorithm is O(n)

def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

    return -1


arr = [10, 20, 80, 30, 60, 50,110, 100, 130, 170]
x = 110
index = linearSearch(arr, x)
print(index)