# Declaring the list
list1 = ['Abhishek', 'Kumar', 'Seth', 'Python']

# Directly printing the list
print ("Simple List:", list1) #Simple List: ['Abhishek', 'Kumar', 'Seth', 'Python']

# Printing the list by join method
print ('List by using join method: %s' % ', ' .join(list1))  #List by using join method: Abhishek, Kumar, Seth, Python

# Direct use of join method
print ('Direct apply the join method:',(", " .join(list1))) #Direct apply the join method: Abhishek, Kumar, Seth, Python


print("******************************************")
# Zip tricks

# Declaring the list geek
list2 = ['Sun', 'Flowers', 'Peoples', 'Animals', 'Day', 'Night']
partition = list(zip(*[iter(list2)] * 2))
print(partition) #[('Sun', 'Flowers'), ('Peoples', 'Animals'), ('Day', 'Night')]

list2 = ['Sun', 'Flowers', 'Peoples', 'Animals', 'Day']
partition = list(zip(*[iter(list2)] * 2))
print(partition) #[('Sun', 'Flowers'), ('Peoples', 'Animals')]


print("****************************************")
#Printing more than one list’s items simultaneously
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

# Here zip() function takes two equal length list and merges them together in pairs
for a, b in zip(list1,list2):
    print (a, b)

#output
# 1 2
# 3 4
# 5 6
# 7 8

print("****************************************")
# Take the string as input and convert it into list:
#In Python 2.7 replace input() to raw_input()
# Reads a string from input and type case them to int after splitting to white-spaces

formatted_list = list(map(int, input().split()))
print(formatted_list)

# input 2 4 5 6
# output [2, 4, 5, 6]

print("****************************************")
# Convert list of list into single list

# import the itertools
import itertools

# Declaring the list list3
list3 = [[1, 2], [3, 4], [5, 6]]

# chain.from_iterable() function returns the elements of nested list
# and iterate from first list of iterable till the last
# end of the list

lst = list(itertools.chain.from_iterable(list3))
print(lst) #[1, 2, 3, 4, 5, 6]

print("****************************************")
# Printing the repeated characters
# + used for string concatenation
# To repeat the character n times, just multiply n with that character
print ("G" + "e"*5 + "k"*4 + "s"*2) #Geeeeekkkkss

print("*********************************************")

# Python program to convert decimal number into binary, octal and hexadecimal number system

# Change this line for a different result
dec = 344

print("The decimal value of",dec,"is:")
print(bin(dec),"in binary.")
print(oct(dec),"in octal.")
print(hex(dec),"in hexadecimal.")

print("******************************************************")

# Program to find the ASCII value of the given character

# Change this value for a different result
c = 'p'

# Uncomment to take character from user
#c = input("Enter a character: ")

print("The ASCII value of '" + c + "' is",ord(c))


print("The character of 65 is ",chr(65))

print("**************************")

mylist = ['abhi', 'ram', 'abkd','help', 'apple','apk','monika','sumit', 'helpdesk']
matching_word = [x for x in mylist if 'k' in x]
print(matching_word)

matchers = ['ab','hel']
matching = [s for s in mylist if any(xs in s for xs in matchers)]
print(matching)

