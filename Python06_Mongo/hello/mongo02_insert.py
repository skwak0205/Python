# -*- coding: utf-8 -*-

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test
collection = db.score

# res01 = collection.insert_one({'name': '춘향이', 'kor': 56, 'eng':87, 'math': 100})
# print(res01.inserted_id)

for doc in collection.find():
    print(doc)

# res02 = collection.insert_many([
#     {'name': '???', 'kor': 96, 'eng':47, 'math': 100},
#     {'name': '아이언맨', 'kor': 12, 'eng':100, 'math': 40},
#     {'name': '배트맨', 'kor': 100, 'eng':52, 'math': 60}
# ])

# print(res02.inserted_ids)

