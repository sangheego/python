#숫자 리스트로 제곱한 리스트 만들기
li=[i for i in range(10000)] # 0~9999까지 리스트 생성
temp=[]
for x in li:
    temp.append(x*x)
print(temp)

def f(x):
    return x*x
temp=list(map(f,li))  #li의 모든 요소에 f함수를 적용해 변환한 결과를 temp에 대입
print(temp)
#한 줄 람다 처리
temp=list(map(lambda x:x*x,li))

#게시판 찾기 - 줄 수가 1줄 이상이라 람다로 불가
ar=["Hello","nancy","123"]
def f(x):
    if len(x)>3:
        return x[0:3] + "..."
    return x
temp=list(map(f,ar))
print(temp)