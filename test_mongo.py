from pymongo import MongoClient

HOST = '172.17.0.2'

client = MongoClient(HOST)
client.some_db.some_collection.insert({'lorem': 'ipsum'})
result = client.some_db.some_collection.find({'lorem': 'ipsum'})
print(list(result))
