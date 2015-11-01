import pymongo
import datetime

from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.learn
employees = db.employees
# print collection

post = {"author": "Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"],"date": datetime.datetime.utcnow()}
post_id = employees.insert_one(post).inserted_id
print post_id
