# 다음과 같은 테스트에서 모든 태그를 제외한 텍스트만 출력하세요.

s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
            To connect to the most powerful tolls int the world.
        </p>
    </body>
</html>"""

isTag = False
result = ''

for c in s:
    if c == '<':
        isTag = True
        result += ' '
    elif c == '>':
        isTag = False
        result += ' '
    elif c == '\n':
        result += '\n'
    elif isTag == False:
        result += c

print(result)

