import sys
print(sys.stdin.encoding)
print(sys.stdout.encoding)

print("한글".encode())
print("한글".encode().decode())

print(ord("a"),ord("한"))

import re
# :이나 |를 ,로 치환
testStr="apple:samsung google|kakao"
result=re.sub("[:,|]",",",testStr)
print(result)

# 이메일이 유효한 이메일인지 검사
p=re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
emails=["gsh5004@naver.com","sanghee@kakao.com", "gohc5004@gmail.com","sanghee@naver"]
for email in emails:
    print(p.match(email)!=None)