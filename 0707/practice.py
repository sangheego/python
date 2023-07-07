'''for i in range(1,26):
    print("*", end="")
    if i%5==0:
        print()

for i in range(5):
    for j in range(5-i):
        print("*", end="")
    print()

for i in range(5):
    for j in range(2*i+1):
        print("*", end="")
    print()

for i in range(5):
    if i <3:
        for j in range(i+1):
            print("*", end="")
    else:
        for j in range(5-i):
            print("*", end="")
    print()

#피라미드모양
숫자로 변환하고자 하는 경우는
cnt=0
for i in range(5):
    cnt를 증가시키고 cnt%10을 출력
    if i ==0 or i==4:
        공백 출력
        별 출력
    else:
        공백 출력
        별 출력
        공백출력
        별 출력
    print()

for i in range(5):
    if i ==0 or i==4:
        print("*"*(2i-1))
        별 출력
    else:
        공백 출력
        별 출력
        공백출력
        별 출력
    print()'''
for i in range(5):
    print("*" * (2*i-1))

''''#완전수의 합 구하기: 약수의 합이 자신의 값과 같은 것 ex.6
cnt=0 #완전수의 개수를 저장할 변수
for i in range(2,1001):
    hap=1 #약수의 합을 저장할 변수
    for su in range(2,i//2+1):
        if i%su==0:
            hap=hap+su
    #완전수 판별
    if i==hap:
        cnt=cnt+1
print(cnt)

피보나치 수열: 첫 번째와 두 번째 데이터는 1
세번째 데이터부터는 앞의 2개의 합
1,1,2,3,5,8,13,21,34
n번째 피보나치 수열의 값을 구하는 로직을 지정

n=int(input("구하고자 하는 피보나치 수열의 값은?"))
if n == 1 or n ==2:
    print(1)
else:
    n_1=1 #직전 항
    n_2=1 #두번째 앞의 항
    result=0
    for i in range(3, n+1):
        result =n_1+n_2
        n_2=n_1
        n_1=result
    print(result)'''