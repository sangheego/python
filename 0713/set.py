#set은 데이터 순서 상관없이 저장되므로 출력되는 순서도 예측 불가
s={"nancy",'apple','exo','apple'}
print(s)
s.add("numbers")
for d in s:
    print(d)

dic={}
dic['name']='adam'
dic['job']='singer'
dic['father']='pms'
dic['father']='pjm'
print(dic)
print(dic['job'])
print(dic.get('job','nojob'))
# print(dic['score']) #존재하지 않는 key를 사용하면 keyError발생
print(dic.get('score',0)) #존재하지 않는 key를 사용하면 두 번째 매개변수 리턴
#순회
for key in dic:
    print(key, dic[key])