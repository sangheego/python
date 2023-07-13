'''li=['nancy','ecc','wonderland','cheer']
li.sort() #오름차순 정렬
print(li)
li.sort(reverse=True)  #내림차순 정렬
print(li)

result=sorted(li) #sorted는 정렬한 결과를 리턴
print(result)
#대소문자 구분없이 정렬
li.sort(key=str.lower)
print(li)

li1.append("navigation")
print(li1)
print(li1[0])
print(li1[0:2])

del li1[3]
print(li1)

#데이터 순회
for project in li1:
    project(project)'''

li=list(range(10))
result=list(map(lambda x:x**2,li))
print(result)

for i in li:
    result.append(i*i)
print(result)

#list comprehension 이용
result=[i*i for i in li]
print(result)

#for 2개 사용
li1=[1,2,3]
li2=[4,5,6,7]
result=[x*y for x in li1 for y in li2]
print(result)

#for 와 if - filtering
singers=['ive','sohee','suzy','iu']
result=list(filter(lambda x:len(x)>=3,singers))  # 함수 만든 것
result=[x for x in singers if len(x)>=3]  # 더 빠름
print(result)
#2개의 조건 적용
result=[x for x in singers if len(x)>=3 if len(x)<4]
print(result)
#3글자 이상은 그대로 나머지느 _를 추가
result=[x if len(x) >=3 else x + "_" for x in singers]
print(result)