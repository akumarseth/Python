import redis

myHostname = "<HOSTNAME>.redis.cache.windows.net"
myPassword = "<ACCESSKEY>"

r = redis.StrictRedis(host=myHostname, port=6380,password=myPassword,ssl=True)

result = r.ping()
print("Ping returned : " + str(result))

result = r.set("Message", "Value for the message key")

result = r.set("New Message", "Hello!, This is new Message")

print("SET Message returned : " + str(result))

result1 = r.get("Message")
result2 = r.get("New Message")
print("GET Message returned : " + result1.decode("utf-8"))
print("GET Message returned : " + result2.decode("utf-8"))

result = r.client_list()
print("CLIENT LIST returned : ") 
for c in result:
    print("id : " + c['id'] + ", addr : " + c['addr'])