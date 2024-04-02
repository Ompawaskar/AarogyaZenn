from pymongo import MongoClient


def connection():
    try:
        connection_string ='mongodb+srv://ompawaskar:ruchita@cluster0.lsshopg.mongodb.net/'
        client = MongoClient(connection_string, tlsAllowInvalidCertificates=True)
        db = client["AarogyaZen"]
        return db
    except Exception as e:
        print("Error connecting to MongoDB:", e)
        return None
