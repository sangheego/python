'''def outer():
    outer_data="외부 함수의 데이터"
    def inner():
        nonlocal outer_data
        outer_data="함수 외부의 데이터"
        print(outer_data)
    inner()
    print(outer_data)
outer()'''

outer_data="전역에 만든 데이터"
def outer():
    def inner():
        global outer_data
        outer_data="함수 외부의 데이터"
        print(outer_data)
    inner()
    print(outer_data)
outer()

def outer():
    data=0
    #자신을 감싸고 있는 함수의 데이터를 수정하는 함수
    def inner():
        nonlocal data
        data=data+1
        print(data)
    #함수 내부의 데이터를 수정하는 함수를 리턴하는 함수를 closure라고 함
    return inner
closure=outer() #함수를 호출해서 리턴하는 함수를 변수에 저장
closure()
closure()

def deco(func):
    print("공통관심사항")
    func()
@deco
def businessLogic():
    print("업무 로직")
businessLogic()
#고객의 니즈 변경
#업무 로직과 관계 없는 로깅을 출력하는 코드를 추가하기를 원하는 방향으로 변경
#유지보수 과정이나 업무 로직과 관련이 없는 코드를 추가하거나 삭제하는 경우
#업무 로직을 직접 수행하는 것은 예상치 못한 결과를 만들어 낼 수 있음
#이런 경우에는 업무 로직은 손을 대지 않고
def decorator(func):
    func()
    print("로깅")
@decorator
def businessLogic():
    print("업무 로직")
businessLogic()