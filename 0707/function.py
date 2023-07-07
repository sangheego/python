def display():
    for i in range(3):
        print("Hello Python")

display()
print(display)

def intAddWithInt(a,b):
    return a+b
result=intAddWithInt(100,300) #스택 하나 열렸다가 400되고 닫힘
x=intAddWithInt(result,600)  #스택 열림
print(x)

print(intAddWithInt(intAddWithInt(100,300),600)) #하나 스택이 열린채로 스택이 동시에 2개 열려야 하는 순간이 있음
#아래보다 위에가 스택이 덜 열려서 메모리가 더 절약됨

#파이썬은 여러 개 데이터 나열해서 리턴하는 것이 가능
#여러 개 나열해서 리턴하면 하나의 튜플로 만들어서 리턴

def intOpWithInt(a,b):
    return a+b, a-b
#튜플 전체를 하나의 변수로 받기
t=intOpWithInt(100,200)
print(t)
#튜플을 분해해서 받기
add,sub=intOpWithInt(100,200)
print(add,sub)

def add(a:int, b:int)->int:
    return a+b
print(add(100,300))

def callByValue(a:int)-> None:
    a=20
    print(a)
x=30
callByValue(x)
print(x)
def callByReference(li:list)->None:
    li[0]=20
    print(li)
l=[100,200,300]
callByReference(l)
print(l)

#함수 호출시 매개변수 이름과 값을 같이 전달 가능
print("nancy","Jennie","pink",sep="\t") #사이사이 탭 추가

def collection(a,b):
    print(a)
    print(b)
collection(10,20)
collection(*[100,200]) #list를 분할해서 a에 100 b에 200 대입
collection(*{'key1':100,'key2':200}) # *하나면 key값이 매개변수에 전달
collection(**{'a':100,'b':200}) # *둘이면 value값이 매개변수에 전달
# 이때 key이름과 매개변수 이름이 같아야 함

def merge(*li):
    for element in li:
        print(element)

merge(10)
merge(10,20)
merge(10,20,30)

merge("nancy",10,20,30) #name에 nancy대입, 나머지는 li에 대입
# merge(name="nancy", 10,20,30) #에러

def merge(name, **param):
    for k in param:
        print(k, param[k])
merge(name='nancy', job='singer', gender='girl')

def hap(n:int)-> int:
    if n ==1:
        return 1
    return n + hap(n-1)
print(hap(10))
def x():
    for i in range(10):
        if i ==5:
            return  #break역할 수행
#피보나치 수열을 재귀로 구하는 함수
import functools
@functools.lru_cache() #메모이제이션: 함수의 호출 결과를 저장해 둔 후 재사용하는 것
def fibonacci(n:int)-> int:
    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)
print(fibonacci(10))

fibonacci.__doc__="재귀를 이용해서 피보나치 수열의 값을 리턴하는 함수"
help(fibonacci)

def dragonAttack():
    print("드래곤 공격")
def tankAttack():
    print("탱크 공격")
delegate=dragonAttack
delegate()
delegate=tankAttack
delegate()

#high order function
def outer():
    def inner():
        print("내부 함수")
    return inner
#함수를 호출해서 그 결과를 변수에 대입하고 그 변수를 통해서 함수 호출
func=outer()
func()