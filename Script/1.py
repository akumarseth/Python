from urllib.request import urlopen
import jwt, datetime

print(datetime.datetime.utcnow() + datetime.timedelta(seconds=100))
print(datetime.timedelta(seconds=100))

expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=100)
token = jwt.encode({'exp': expiration_date}, 'meow', algorithm='HS256')
print(token)
# code to test slicing

# tuple1 = (0 ,1, 2, 3)
# print(tuple1[1:])
# print(tuple1[:2])
# print(tuple1[-3:])
# print(tuple1[::-1])
# print(tuple1[2:4])
print(2^2)

print("********************************")
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
print(A0)
print(A1)
print(A2)
print(A3)
print(A4)
print(A5)
print(A6)


