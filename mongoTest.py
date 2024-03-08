from pymongo import MongoClient

client = MongoClient("mongodb+srv://ompawaskar7:pawasakar123@cluster0.lsshopg.mongodb.net/")

db = client["AarogyaZen"]
user_collection = db["user"]

print(user_collection)


