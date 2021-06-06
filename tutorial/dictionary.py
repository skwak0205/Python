# 사전
cabinet = {3: "유재석", 100:"김태호"}
print(cabinet[3])

print(cabinet.get(3))

print(cabinet[5]) # 에러 발생
print(cabinet.get(5)) # None 리턴
print(cabinet.get(5, "사용 가능")) # 5번 키의 값이 없을 시 "사용 가능" 출력

print(3 in cabinet) # 3이라는 키가 있는지 확인
print(5 in cabinet)

cabinet = {"a-3": "유재석", "b-100": "김태호"}

cabinet["a-3"] = "김종국"
cabinet["c-20"] = "조세호"

# 값 삭제
del cabinet["a-3"]

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 모두 지우기
cabinet.clear()