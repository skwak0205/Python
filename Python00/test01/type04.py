# tuple : list와 거의 같음

# 생성자 사용
a = tuple()
print(a)
b = tuple([1,2,'3'])
print(b)

# 값을 추가, 수정, 삭제 (변경) 불가능
# a.append(1)

# () 사용
d = tuple(range(3,6))
print(d)
print(b+d)

# tuple -> list
e = list(d)
e.append(6)
print(e)

# list -> tuple
f = tuple(e)
print(f)

#  unpacking (안에 있는 값 개수만큼 안해주면 에러남)
g,h,i,j = f
print(g)
print(h)
print(i)
print(j)


