problem="GDKKDGCCGDDFDDGCCGCCGDDDGCCGFFF"
#GCCG의 위치를 전부 출력
#한번 포함되는 포함된 문자는 빼고 찾기
#GCCGCCG는 1번만 찾아야 함
#for, while은 1번만 들어가야 함

import re

'''for problem in re.finditer('GCCG',problem):
    print (problem.start())'''
result= re.findall('GCCG',problem)
print(result)

