record=("adam","singer",2)
print(record)
print(record[0])
#record[0]='아담' #수정 불가

#리스트와 튜플은 unpacking 가능
name, job, albumCnt=record
print(albumCnt)
*etc,albumCnt=record  #*을 이용하면 나머지 모두를 list로 생성
print(etc)
#swap: 2개의 데이터의 값을 치환
a=10
b=20
a,b=b,a
print(a,b)

data=[('adam','010'),('nancy','013')]
for row in data:
    print(row[0])

from collections import namedtuple
Person=namedtuple("person","name mobile")
persons=[Person('adam','010'),Person('nancy','013')]
for person in persons:
    print(person.name)