# -*- coding: utf-8 -*-

import pickle

score = {'name': 'kh', 'kor': 100, 'eng': 100, 'math': 30}

with open('test02.txt', 'wb') as file:
    pickle.dump(score, file)

'''
pickling : 객체 -> 파일
unpickling : 파일 -> 객체
'''