import random

# 1 ~ 45 사이의 중복되지 않는 6개 숫자 출력
def lotto():
    res = set()

    while len(res) <= 6:
        ran = random.randint(1, 45)
        res.add(ran)
    lst = sorted(res)
    print(lst)
    
if __name__ == '__main__':
    lotto()