import random
'''import time
li=['치킨','떡볶이','순대']
for i in range(10):
    time.sleep(1)
    print(li[random.randint(0,len(li)-1)])'''

i=input("1부터 45까지의 정수를 공백으로 구분해서 6개 입력하세요: ")
x=i.split(" ")
lotto=list(map(lambda e:int(e), x))
lotto.sort()
print(lotto)

ar=range(1,46)
cnt=0
while True:
    k=random.sample(ar,6)
    k.sort()
    cnt=cnt+1
    if lotto==k:
        break
print(cnt)

