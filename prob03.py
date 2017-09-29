# 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.

s='/usr/local/bin/python'
t= s.replace('/',' ')
t= t.replace(' ', ', ')
print(t[2::])

# 디렉토리 경로명과 파일명을 분리하여 출력하세요.
t2 = s.rsplit('/',1)
print(t2)
