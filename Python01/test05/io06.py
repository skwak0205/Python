# -*- coding: utf-8 -*-

import pickle

file = open('test02.txt', 'rb')
# print(file.read())
score = pickle.load(file)
print(score)
print(type(score))

file.close()