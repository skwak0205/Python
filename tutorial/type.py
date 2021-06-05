# 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

# 문자열 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9) #반복 출력

# boolean 자료형
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True) # False 출력
print(not False)
print(not (5 > 10)) # True 출력

# 변수
animal = '강아지'
name = '연탄이'
age = 4
hobby = '산책'
is_adult = age >= 3

print('우리집 ' + animal + '의 이름은 ' + name + '예요')
print(name + '는 ' + str(age) + '살이며, ' + hobby + '을 아주 좋아해요')

# ,로 사용 가능 / 타입 상관 없이 쓸 수 있음 / 자동으로 공백 추가됨
print(name, '는 ', age, '살이며, ', hobby, '을 아주 좋아해요')

print(name + "는 어른일까요? " + str(is_adult))

# Quiz 1
'''
변수를 이용하여 다음 문장을 출력하시오

변수명 : station
변수값 : '사당', '신도림', '인천공항' 순서대로 입력
출력 문장 : XX 행 열차가 들어오고 있습니다.
'''

station = '사당'
print(station + " 행 열차가 들어오고 있습니다.")