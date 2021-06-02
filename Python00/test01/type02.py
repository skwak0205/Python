# 문자

# single * 1
a = 'python \'s\nHello, World!'
print(a)

# single * 3
b = '''python's
Hello,World!
    hello python!
        hello Qclass
'''
print(b)

# double * 1
c = "abc\"def\"ghi"
print(c)

# double * 3
d = """abc   "def"   ghi"""
print(d)

e = 'abc"def"ghi\npython\'s string'
print(e)

f = "abc'def'ghi\npython's string"
print(f)

# r(raw) string
g = r"c:\test"
print(g)
h = "c:\test"
print(h)

# str 연산
str01 = "Hello, "
str02 = "World!"

print(str01 + str02)
print(str01 * 3 + str02)

