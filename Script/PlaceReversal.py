def reverse(alist):

   #intializing pointers
   left = 0
   right = len(alist)-1

   #condition for termination
   while left<right:

       #swapping
       temp = alist[left]
       # alist[left] = alist[right]
       # alist[right] = temp

       alist[left],alist[right] = alist[right],temp

       #updating pointers
       left += 1
       right -= 1

   return alist

print(reverse([1,2,3,4,5]))

alist = [1,2,3,4,5,6,7]

print(alist[::-1]) #prints [7,6,5,4,3,2,1]

print(alist) #prints [1,2,3,4,5,6,7]