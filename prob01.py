# 키보드로 정수 수치를 입력 받아 그것이 짝수인지 홀수인지 판별하는 코드를 완성하세요.

import sys

number = input('수를 입력하세요: ')
if number.isdigit() :
    number=int(number)
    if number % 2 == 0:
        print('짝수입니다.')
    else:
        print('홀수입니다.')
else:
    sys.exit(0)

#sys.exit(0)