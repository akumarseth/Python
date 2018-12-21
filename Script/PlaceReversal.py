def reverse(arr):
   #intializing pointers
   left = 0
   right = len(arr)-1
   #condition for termination
   while left<right:
       #swapping
       temp = arr[left]
       arr[left],arr[right] = arr[right],temp

       #updating pointers
       left += 1
       right -= 1
   return arr

print(reverse([1,2,3,4,5]))
alist = [1,2,3,4,5,6,7]
print(alist[::-1]) #prints [7,6,5,4,3,2,1]
print(alist) #prints [1,2,3,4,5,6,7]