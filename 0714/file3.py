'''with open('./log.txt') as f:
    for line in f:
        print(line)

with open('./log.txt') as f:
    cnt=0
    for line in f:
        ar=line.split()
        if ar[8]=='200':
            cnt=cnt+1
print('200의 개수:',cnt)

with open('./log.txt') as f:
    ipCount=0
    for line in f:
        ar=line.split()
        #기존의 값을 가져오는데 없으면 0
        ipCount[ar[0]]=ipCount.get(ar[0],0)+1
for ip in ipCount:
    print(ip,ipCount[ip])'''
#ip별 트래픽 합계
ipTraffic={}
with open('./log.txt') as f:
    for line in f:
        ar=line.split()
        try:
            ipTraffic[ar[0]]=ipTraffic.get(ar[0],0)+int(ar[9])
        except Exception as e:
            print(e)
for ip in ipTraffic:
    print(ip,":",ipTraffic[ip])

#상위 10개 뽑기
'''from collections import Counter
with open('./log.txt') as f:
    for line in f:
        ar=line.split()
        if ar[0]=

print(list)'''
