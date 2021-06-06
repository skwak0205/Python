def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()


def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {}원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {}원입니다.".format(balance-money))

        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {}원 입니다.".format(balance))

        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance-money-commission # tuple 형식으로 반환

balance = 0
balance = deposit(balance, 1000)
print(balance)

balance = withdraw(balance, 2000)


# 기본값
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {}\t 나이 : {}\t주 사용 언어 : {}".format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")
profile("유재석")

# 키워드값
profile(main_lang="자바", age=25, name="김태호")

# 가변 인자
def profile(name, age, *language):
    print("이름 : {}\t나이: {}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end = " ")
    print()

