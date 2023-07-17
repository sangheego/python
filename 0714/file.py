import os
#print(os.getcwd()) 상대 경로를 설정할 때 기준 경로
try:
    file=open('./data.test.txt','w',encoding='utf-8')
    file.write('문자열')
    lines=['nancy','\t','exo','\t','grace']
    file.writelines(lines)
except Exception as e:
    print("파일 처리 중 예외 발생",e)
finally:
    file.close()

try:
    file = open('./data.test.txt', encoding='utf-8')
    content=file.read()
    print(content)
except Exception as e:
    print("파일 처리 중 예외 발생", e)
finally:
    file.close()

