# def hap01(a, b):
    # return a+b
hap01 = lambda a, b: a+b
print(hap01(10, 20))

hap02 = lambda a, b, c: a+b+c
print(hap02(30, 40, 50))

gob = lambda a, b: a*b
print(gob(12, 34))

a = [(1, 'one', 9), (2, 'two', 8), (3, 'three', 7), (4, 'four', 6)]
print(a)
a.sort(key=lambda a: a[1]) #영어들 기준으로 정렬
print(a)

#결과값을 가지고 있음
min01 = (lambda x, y: x if x < y else y)(33,44) #if조건이 참이면 x 리턴, 거짓이면 y 리턴
print(min01)

max01 = lambda x, y: x if x > y else y
print(max01(55, 66))

# 중첩 함수
b = lambda x: (lambda newx: x + newx)
print(b(100)(200))

# c = lambda newx: 100 + newx
c = b(100)
d = c(200)
print(d)

# 1 ~ 100 사이의 5의 배수 출력
e = lambda x: bool(x % 5) # 5%5 = 0 -> boolean타입에서 0은 false
five = [i for i in range(1, 101) if not e(i)] #for문의 결과 i는 앞쪽 i로
print(five)

f = lambda x: x if (x % 5 != 0) else None # None은 null과 비슷
res = [i for i in range(1, 101) if not f(i)]
print(res)

result = [i for i in range(1, 101) if not (lambda x: x if(x % 5 != 0) else None)(i)]
print(result)