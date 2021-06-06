sentence = '나는 소년입니다'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

# 슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0부터 2 이전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) # 처음부터 6 이전까지
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
print("뒤 7자리 (뒤에서 부터) : " + jumin[-7:]) # 맨 뒤에서 7번째 부터 끝까지

# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python)) # 문자열 길이 반환
print(python.replace("Python", "Java")) # Java is Amazing

index = python.index("n")
print(index)
index = python.index("n", index + 1) # 6번째 위치에서 부터 찾음
print(index)

print(python.find("n"))
print(python.find("Java")) # -1 리턴
print(python.index("Java")) # 오류 발생

print(python.count("n")) # n이 총 몇 번 있는지

# 문자열 포맷
print("a" + "b")
print("a", "b")

# 방법 1
print("나는 %d살입니다." % 20) # d : 정수값 의미
print("나는 %s을 좋아해요." % "파이썬") # s : 문자열 의미
print("Apple은 %c로 시작해요." % "A") # c : 한글자만

# %s
print("나는 %s살입니다." % 20)

print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨간", age = 20))

# 방법 4 (v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")

# 탈출 문자
# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# "" 출력
print("저는 '나도코딩' 입니다")
print('저는 "나도코딩" 입니다')
print("저는 \"나도코딩\" 입니다")

# \\ : 문장 내에서 \
print("c:\\workspaces\\workspace_Python")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") #PineApple

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple") #RedApple

# \t : 탭
print("Red\tApple")

# 퀴즈
'''
사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
규칙1 : http:// 부분은 제외 -> naver.com
규칙2 : 처음 만나는  점(.) 이후 부분은 제외 -> naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

생성된 비밀번호 : nav51!
'''

url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙 1
my_str = my_str[:my_str.index(".")] # 규칙 2
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!' # 규칙 3

print("{}의  비밀번호는 {}입니다.".format(url, password))

