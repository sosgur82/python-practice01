# 키보드에서 5개의 정수를 입력 받고 평균을 구하는 프로그램을 작성하시오

l = []
s = 0
while len(l) != 5:
    n= input('>')
    if n.isdigit() is False:
        print('에러: 숫자가 아닙니다. 다시 입력하세요')
        continue
    l.append(int(n))
print(sum(l, 0)/len(l))

