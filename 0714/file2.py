'''import os
try:
    file=open('./data.test.txt','r',encoding='utf-8')
    for line in file:
        print(line)
        print()
except Exception as e:
    print("파일 처리 중 예외 발생",e)
finally:
    file.close()

with open('./data.test.txt','r',encoding='utf-8') as file:
    for line in file:
        print(line)
        print()
#텍스트 파일 읽어서 리스트로 변환
#마지막 데이터에 \n을 제거해주어야 함
data=[]
with open('./new.txt',encoding='utf-8') as file:
    for line in file:
        ar=line.split(",")
        data.append(ar)
print(data)

import csv
data=[]
with open('./new.txt',encoding='utf-8') as file:
    rdr=csv.reader(file)
    for line in rdr:
        data.append(line)
print(data)
import csv
data=[]
with open('./new.txt','a', encoding='utf-8') as file:
    wr=csv.writer(file)
    wr.writerow(['지락실','넷플릭스','집'])
print(data)'''

data=[]
with open('./new.txt','wb') as file:
    file.write("hi".encode())
with open('./new.txt','rb') as file:
    content=file.read()
    print(content.decode())