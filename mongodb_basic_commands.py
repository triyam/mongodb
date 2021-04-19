import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId


cluster = MongoClient(
    host="localhost",
    port=27017,
    serverSelectionTimeoutMS = 1000
)

db = cluster['test']
collection = db['test']

# post = {"_id":"1","name":"Redmi Note 6 pro", "price":11000}
post2 = {"_id":"2","name":"Redmi Note 7 pro", "price":12000}
post3 = {"_id":"3","name":"Redmi Note 8 pro", "price":11000}

#################################################
# to insert 1 post data

collection.insert_one(post1)

#################################################
# to insert many post data

collection.insert_many([post2, post3])

#################################################
# to have search-query ****need regular expresion*****

results = collection.find({"name":"Redmi Note 7 pro"})

for result in results:
    print(result["price"])

#################################################
# to have search-query of one result

results = collection.find_one({"name":"Redmi Note 7 pro"})
print(results["price"])

#################################################
# to have search-query of every-result

results = collection.find({})

for x in results:
    print(x)

#################################################
# to have delete a result

results = collection.delete_one({"name":"Redmi Note 7 pro"})

#################################################
# to have delete all result

results = collection.delete_many({})

#################################################
# update_one for one value and update_many for all values

results = collection.update_many({"name":"Redmi Note 7 pro"}, {"$inc":{"price":"17000"}})

#################################################
# count all id

post_count = collection.count_documents({})
print(post_count)