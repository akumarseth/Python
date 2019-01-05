from urllib.request import urlopen
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
