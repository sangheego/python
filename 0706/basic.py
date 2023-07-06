print([1,2,3]+[4,5])
#print("문자열"+3)=> 에러

print((1,2,3)*3)
print('Hello Python\n'*5)

print(20 & 17)
print(20 | 17)
print(20 ^ 17)
print(~17)

cnt = 0
loop = 0
for idx in range(1,101):
    loop+=1
    if idx %3==0:
        loop=loop+1
        if idx %4==0:
            cnt=cnt+1
print("12의 배수의 개수:", cnt)
print("조건 확인 개수:", loop)

cnt = 0
loop = 0
for idx in range(1,101):
    loop+=1
    if idx %4==0:
        loop=loop+1
        if idx %3==0:
            cnt=cnt+1
print("12의 배수의 개수:", cnt)
print("조건 확인 개수:", loop)

print(type(10.3))
print(type(10))

#묵시적 형변환
x=10 #int
y=10.3  #float
result=x+y
print(result)

help(print)