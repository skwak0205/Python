# 집합 set
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set) # 1,2,3 출력

java = {"유재석", "김태호", "양세호"}
python = set(["유재석", "박명수"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

# 추가
python.add("김태호")

# 삭제
java.remove("김태호")

# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

# 퀴즈
from random import *

users = range(1, 21)
users = list(users)

users = shuffle(users)
winners = sample(users, 4)

print("---당첨자 발표---")
print("치킨 당점자 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:]))
print("---축하합니다---")