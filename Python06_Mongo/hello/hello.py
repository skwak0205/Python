# -*- coding: utf-8 -*-

# pip install pymongo
from pymongo import MongoClient

# MongoDB와 연결
# client = MongoClient('mongodb://localhost:27017')
client = MongoClient('localhost', 27017)

# Database와 연결
db = client.test
# db = client['test']

# Collection과 연결
collection = db.score
# collection = db['score']

# cursor : 요청해서 받아온 일회용 객체
result = collection.find()
# print(result)

for res in result:
    print(res)
