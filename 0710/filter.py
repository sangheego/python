ar=['nancy','jessica','anna',None]
#이름이 5자 이상인 것만 추출- 람다 바꾸기 가능
print(None in ar)
def f1(x):
    return x !=None
#ar=list(filter(f1,ar))
ar=list(filter(lambda x:x!=None,ar))
print(ar)
def f2(x):
    return len(x)>=5
#result=list(filter(f2,ar))
result=list(filter(lambda x:len(x)>=5, ar))
print(result)

#이름이 ㅇ로 시작하는 것만 추출
name=['안중근','김구','윤봉길']
result=list(filter(lambda x:x[0]>="아"and x[0]<"자",name))
print(result)

#데이터가 컬렉션에 포함되어 있는지 확인: in (반대는 not in)
num=['1','2','3']
kwlist=['1']

key=['초등학교','중학교','고등학교']
value=['돈암초','배화여중','하나고']
print(list(zip(key,value)))
print(dict(zip(key,value)))

def outer():
    outer_data="외부 함수의 데이터"
    def inner():
        inner_data="내부 함수의 데이터"
        print(outer_data)
    #print(inner_data)