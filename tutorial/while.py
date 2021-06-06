# while
customer = "토르"
index = 5
while index >= 1:
    print("{}, 커피가 준비되었습니다. {}번 남았어요".format(customer, index))
    index -= 1

    if index == 0:
        print("커피는 폐기처분되었습니다.")


customer = "아이언맨"
index = 1
while True:
    print("{}, 커피가 준비되었습니다. 호출 {}회 ".format(customer, index))
    index += 1

