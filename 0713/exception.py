def div(x):
    return 10/x
try:
    print(div(20))
    print(div(0))
except:
    print("예외 발생")
print("프로그램 종료")

ar=[10,20,30]
try:
    su=int(input("나눌 수를 입력하세요: "))
    i=0
    j=len(ar)
    while i<j:
        if su==1:
            raise ValueError("강제로 예외 발생")
        assert su !=2, 'su는 2면 안 됩니다'
        # 2면 메시지 출력하고 프로그램은 중단됨
        print(ar[i]/su)
        i=i+1
except ValueError as e:
    print("잘못된 데이터 입력")
    print(e)
except ZeroDivisionError as e:
    print("0으로 나눌 수 없음")
    print(e)
else:
    print("예외가 발생하지 않은 경우 수행할 내용")
finally:
    print("무조건 수행")
