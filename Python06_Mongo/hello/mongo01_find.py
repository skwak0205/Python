# -*- coding: utf-8 -*-

from pymongo import MongoClient
import pprint


client = MongoClient('localhost', 27017)
test = client.test
score = test.score

cursor = score.find()

for doc in cursor:
    # print(doc)
    pprint.pprint(doc)

print('---------------------')

# shin = score.find({'name': '신동엽'})
shin = score.find_one({'name': '신동엽'})
pprint.pprint(shin)

print('---------------------')

# 국어점수가 60보다 큰 document들을 모두 출력
kors = score.find({'kor': {'$gt' : 60}})
for doc in kors:
    pprint.pprint(doc)

print('---------------------')

print('score collection 안에 있는 document의 총 갯수 : ', score.count_documents({}))