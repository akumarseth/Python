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


