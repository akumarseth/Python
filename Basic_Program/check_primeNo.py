# Python program to check if the input number is prime or not

num = 407

# take input from the user
# num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num//2):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")

# import math module 
import math 
  
# function to check if prime or not  
def check(n): 
    if n == 1: 
        return False
          
        # from 1 to sqrt(n)  
    for x in range(2, (int)(math.sqrt(n))+1): 
        if n % x == 0: 
            return False 
    return True
  
# driver code 
n = 23
if check(n): 
    print("prime")  
else: 
    print("not prime") 
