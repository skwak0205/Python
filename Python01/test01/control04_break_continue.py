i = 1

while i <= 10:
    if i > 5:
        break
    print(i)
    i += 1
else: # 출력안됨 / 반복문이 정상적으로 종료되었을 때만 실행 됨 / 지금은 break가 있어서 안됨
    print('i:', i)

print('----------------')

for i in range(1, 10):
    if i%2 == 0:
        continue
    print(i)
else:
    print('i:', i)