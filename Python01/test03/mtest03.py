'''
1. for문을 사용하여 구구단 전체를 출력하는 gugu()라는 함수를 만들자.
2. while문을 사용하여 함수 호출시 입력된 단만 출력하는 gugudan(x)를 만들자
3. main 함수에서 gugu()와 gugudan(x) 함수를 호출하되, gugudan에 입력해주는 숫자는 input을 사용하자.
'''

def gugu():
    # pass 나중에 실행하겠다는 뜻

    for i in range(2, 10):
        print('<<' + str(i) + '>>단')
        for j in range(1, 10):
            print('{} * {} = {}'.format(i, j, i*j))

def gugudan(x):
    print('<<'+ x + '>>단')
    for j in range(1, 10) :
        print('{} * {} = {}'.format(x, j, int(x)*j))

if __name__=='__main__':
    gugu()
    print('--------------------------------------')
    input = input('원하는 단을 입력해 주세요 : ')
    gugudan(input)
