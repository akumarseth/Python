print("******************************")

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
print(A0)  #Output - {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(A1)  #Output - range(0, 10)
print(A2)  #Output - []
print(A3)  #Output - [1, 2, 3, 4, 5]
print(A4)  #Output - [1, 2, 3, 4, 5]
print(A5)  #Output - {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print(A6)  #Output -  [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]

print("******************************")

#In-Place Swapping Of Two Numbers.

x, y = 10, 20
print(x, y) #10 20
x, y = y, x
print(x, y) #20 10

print("******************************")

# Reversing a string in Python

a ="Abhishek Kumar Seth"
print("Reverse is", a[::-1]) #Reverse is hteS ramuK kehsihbA
lista = a.split(" ")
print((' ').join(lista[::-1])) #Seth Kumar Abhishek

print("******************************")
# Create a single string from all the elements in list

a = ["Abhishek", "Kumar", "Seth"]
print(" ".join(a)) #Abhishek Kumar Seth

print("******************************")

# Chaining Of Comparison Operators.
n = 10
result = 1 < n < 20
print(result) #True
result = 1 > n <= 9
print(result) #False

print("******************************")
# Print The File Path Of Imported Modules.
import os;
import socket;

print(os) #<module 'os' from 'C:\\python37\\lib\\os.py'>
print(socket) #<module 'socket' from 'C:\\python37\\lib\\socket.py'>

print("******************************")
# Use Of Enums In Python
class MyName:
	Abhishek, Kumar, Seth = range(3)

print(MyName.Abhishek) #0
print(MyName.Kumar) #1
print(MyName.Seth) #2


class MyNameTest:
    ABC, xyz, ABC = range(3)

print(MyNameTest.ABC) #2
print(MyNameTest.xyz) #1
print(MyNameTest.ABC) #2

print("******************************")
# Return Multiple Values From Functions.
def x():
	return 1, 2, 3, 4
a, b, c, d = x()

print(a, b, c, d) # 1 2 3 4


print("******************************")
# Find The Most Frequent Value In A List.
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test), key = test.count)) # 4


print("******************************")
# Check The Memory Usage Of An Object

import sys
x = 1.7
print(sys.getsizeof(x))  #16

print("******************************")
# Print string N times.
n = 2
a ="AbhishekKumarSeth"
print(a * n) #AbhishekKumarSethAbhishekKumarSeth

print("******************************")
# Checking if two words are anagrams
from collections import Counter
def is_anagram(str1, str2):
	return Counter(str1) == Counter(str2)
print(is_anagram('Abhishek', 'bhiAkshe')) #True

print(is_anagram('Abhishek', 'kbhishea')) #False

print("*******************************")

list1= [10, 2, 3, 1, 5, 8, 39, 21, 65, 40]
list1.pop()
print(list1) #[10, 2, 3, 1, 5, 8, 39, 21, 65]
list1.pop(2)
print(list1) #[10, 2, 1, 5, 8, 39, 21, 65]

print("*******************************")

def weekdays():
	yield week[0]
	yield week[0+1]

week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
day = weekdays();
print(day) #<generator object weekdays at 0x012633B0>
print(next(day)) #Sun



import jwt, datetime
# import getpass
#
# user = input("Enter Username: ")
# pwd = getpass.getpass("Enter Password: ")

# print(user, '\n', pwd)

print(datetime.datetime.utcnow() + datetime.timedelta(seconds=100))
print(datetime.timedelta(seconds=100))

expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=100)
token = jwt.encode({'exp': expiration_date}, 'meow', algorithm='HS256')
print(token)
# code to test slicing

tuple1 = (0 ,1, 2, 3)
print(tuple1[1:]) #(1, 2, 3)
print(tuple1[:2]) #(0, 1)
print(tuple1[-3:]) #(1, 2, 3)
print(tuple1[::-1]) #(3, 2, 1, 0)
print(tuple1[2:4]) #(2, 3)
print(2^2) #0

print("********************************")

list1 = [1,4,5,2,6,3,5]

print(list1[2:]) # [5,2,6,3,5]
print(list1[:2]) #[1,4]
print(list1[::-1]) #[5, 3, 6, 2, 5, 4, 1]


print("********************************")
list1 = [1,2, 3, 4, 5, 6, 7, 8, 9]
list2 = [8, 9]

print([x for x in list1 if x not in list2]) #[1, 2, 3, 4, 5, 6, 7]
print([x*x for x in list1]) #[1, 4, 9, 16, 25, 36, 49, 64, 81]

list1 = list1 + list2
print(sorted(list(set(list1))))  #[1, 2, 3, 4, 5, 6, 7, 8, 9]

print("********************************")
mylist = ["a", "b", "a", "c", "c"]
my_set = (set(mylist))
print(sorted(list(my_set)))





