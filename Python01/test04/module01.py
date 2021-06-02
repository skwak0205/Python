# math 라는 module  사용
# import math

# math 라는 module에서 pi만 가져와서 사용
from math import pi

def circle(x):
    return pi * x * x

if __name__ == '__main__':
    r = input('반지름 : ')
    print('반지름이 %s인 원의 넓이는 %f 입니다.' % (r, circle(int (r))))
    
