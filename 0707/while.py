idx=0
while idx<10:
    print(idx)
    idx=idx+1
    if idx>5:
        break
else:
    print("반복문 종료")

string = "Hello"
ar= [10,20]
row= (10,20)
s= {10,20}
dict = {"key":"value"}

for news in range(1,32,15):
    print("https://www.donga.com/news/search?p=",news,sep="")
    #sep는 공백 제거
for news in range(3):
    print("https://www.donga.com/news/search?p=",(news*15)+1, sep="")
