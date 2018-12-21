import fbchat
print(fbchat)
from getpass import getpass
username = str(input("Username: "))
password = input("Password: ")
client = fbchat.Client(username, password)
no_of_friends = int(input("Number of friends: "))
for i in range(no_of_friends):
	name = str(input("Name: "))
	friends = client.searchForUsers(name) # return a list of names
	friend = friends[0]
	msg = input("Message: ")
	sent = client.send(friend.uid, msg)
	if sent:
		print("Message sent successfully!")
