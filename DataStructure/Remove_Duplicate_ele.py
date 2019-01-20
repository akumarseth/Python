# Remove duplicate eement from a sorted arr
# using a extra temp array

def rem_dup_using_extra_space(arr):
    j=0
    temp = []
    n = len(arr)
    for i in range(n-1):
        if(arr[i] != arr[i+1]):
            temp.insert(j, arr[i])
            j += 1
    temp.insert(j, arr[n-1])
    return temp

def rem_dup_using_const_space(arr):
    j=0
    n=len(arr)
    for i in range(n-1):
        if(arr[i] != arr[i+1]):
            arr.__setitem__(j,arr[i])
            j += 1
    arr.__setitem__(j, arr[n-1])
    return arr[:j+1] # since after set element of last element all other element is still exist in the arr

# print(help(list.__setitem__))
input_arr =[1,2,2,3,3,3,3,4,5,6,7,7,7,8,8,8,8,8,8,9,10,10,11]
print(input_arr)
distinct_ele = rem_dup_using_extra_space(input_arr)
print(distinct_ele)
distinct_ele = rem_dup_using_const_space(input_arr)
print(distinct_ele)