# list (배열처럼 사용 가능)

# 생성자
a = list()
print(a)
a.append(1)
print(a)
a.append('a')
a[1] = 'b'
print(a)

# 2번 인덱스가 없음
# a[2]='c'
# print(a)

# [] 사용
b = [1,2,3,4,5]
print(b)
print(b[0]+b[3])

b.reverse()
print(b)

b.append(6)
print(b)

b.sort()
print(b)

# 중첩
c = ['a', 'b', 'c','d', ['e', 'f','g']]
print(c)
print(c[4])
print(c[4][0])

# 중복 가능
c.append('a')

# list + list
print(b+c)