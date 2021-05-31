import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["pythondb"]

print(myclient.list_database_names())

# dblist = myclient.list_database_names()
# if "pythondb" in dblist:
#     print("The database exists.")
#
# mycol = mydb["customers"]
# mydict = { "name": "John", "address": "Highway 37" }
# x = mycol.insert_one(mydict)
# print(x.inserted_id)
#
# mylist = [
# { "name": "Amy", "address": "Apple st 652"},
# { "name": "Hannah", "address": "Mountain 21"},
# { "name": "Michael", "address": "Valley 345"},
# { "name": "Sandy", "address": "Ocean blvd 2"},
# { "name": "Betty", "address": "Green Grass 1"},
# { "name": "Richard", "address": "Sky st 331"},
# { "name": "Susan", "address": "One way 98"},
# { "name": "Vicky", "address": "Yellow Garden 2"},
# { "name": "Ben", "address": "Park Lane 38"},
# { "name": "William", "address": "Central st 954"},
# { "name": "Chuck", "address": "Main Road 989"},
# { "name": "Viola", "address": "Sideway 1633"}
# ]
#
# x = mycol.insert_many(mylist)
# print(x.inserted_ids)
#
#
# mylist = [
# { "_id": 1, "name": "John", "address": "Highway 37"},
# { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
# { "_id": 3, "name": "Amy", "address": "Apple st 652"},
# { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
# { "_id": 5, "name": "Michael", "address": "Valley 345"},
# { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
# { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
# { "_id": 8, "name": "Richard", "address": "Sky st 331"},
# { "_id": 9, "name": "Susan", "address": "One way 98"},
# { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
# { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
# { "_id": 12, "name": "William", "address": "Central st 954"},
# { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
# { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
# ]
#
# x = mycol.insert_many(mylist)
# print(x.inserted_ids)
#
# x = mycol.find_one()
# print(x)
#
# for x in mycol.find():
#     print(x)
#
# for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
#     print(x)
#
# for x in mycol.find({},{ "address": 0 }):
#     print(x)
# #Error
# # for x in mycol.find({},{ "name": 1, "address": 0 }):
# #     print(x)
#
# myquery = { "address": "Park Lane 38" }
#
# mydoc = mycol.find(myquery)
#
# for x in mydoc:
#     print(x)
#
# myquery = { "address": { "$gt": "S" } }
# myquery = { "address": { "$regex": "^S" } }
# mydoc = mycol.find(myquery)
#
# for x in mydoc:
#     print(x)
#
# mydoc = mycol.find().sort("name")
# mydoc = mycol.find().sort("name", -1)
#
# for x in mydoc:
#     print(x)
#
# myquery = { "address": "Mountain 21" }
#
# mycol.delete_one(myquery)
#
# myquery = { "address": {"$regex": "^S"} }
#
# x = mycol.delete_many(myquery)
#
# print(x.deleted_count, " documents deleted.")
#
# x = mycol.delete_many({})
#
# print(x.deleted_count, " documents deleted.")
#
# mycol.drop()
#
# myquery = { "address": "Valley 345" }
# newvalues = { "$set": { "address": "Canyon 123" } }
#
# mycol.update_one(myquery, newvalues)
#
# myquery = { "address": { "$regex": "^S" } }
# newvalues = { "$set": { "name": "Minnie" } }
#
# x = mycol.update_many(myquery, newvalues)
#
# print(x.modified_count, "documents updated.")
#
# #print "customers:" after the update:
# for x in mycol.find():
#     print(x)
#
# myresult = mycol.find().limit(5)
# #print the result:
# for x in myresult:
#    print(x)
