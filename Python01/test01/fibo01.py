# fibonacci 수열 : 0 1 1 2 3 5 8 13 21 ...

n = input('input n : ')
print(type(n))

a,b = 0, 1
i = 0
while i < int(n):
    print(a, end=' ')
    a, b = b, a+b
    i += 1
print()

