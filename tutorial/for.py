for waiting_no in [0, 1, 2, 3, 4]:
    print("대기 번호 : {}".format(waiting_no))

for waiting_no in range(1, 6): # 1, 2, 3, 4, 5
    print("대기 번호 : {}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{}, 커피가 준비되었습니다.".format(starbucks))


students = [1, 2, 3, 4, 5]
print(students)

students = [i+100 for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

students = [i.upper() for i in students]
print(students)
