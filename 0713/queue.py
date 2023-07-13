from collections import Counter
data=['a','b','c','a','a','c','d','c','b']
counter=Counter(data)
#dict 변환해서 전체 데이터 개수 파악
print(dict(counter))
#한가지 데이터 파악
print(counter['a'])
#상위 2개만 추출
print(counter.most_common(2))

data=[('apple',3),('apple',2),('orange',3),('mango',3),('orange',5)]
#데이터 등장 횟수
counter=Counter()
for name, count in data:
    counter[name]+=1
    print(counter)
print()
#데이터의 합계
counter=Counter()
for name, count in data:
    counter[name]+=count
print(counter)