def fibo01(n):
    a, b = 0, 1
    i = 0
    while i < n:
        print(a, end=' ')
        a, b = b, a+b
        i += 1
    print()

def fibo02(n):
    res = list()
    a, b = 0, 1
    i = 0
    while i < n:
        res.append(a)
        a, b = b, a+b
        i += 1
        
    return res

if __name__ == '__main__':
    n = int(input('n : '))
    
    # 입력된 숫자 만큼 반복해서 출력
    fibo01(n)

    # 입력된 숫자 만큼 반복해서 list에 저장하고,
    # list를 리턴
    print(fibo02(n))
