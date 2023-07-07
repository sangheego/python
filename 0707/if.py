'''score=int(input("점수를 입력하세요: "))
#print(type(score))
if score >=60:
    print("합격")
else:
    print("불합격")
print("프로그램 종료")

90~100 A
80~90 B
70~80 C
60~70 D
50~60 E

score=int(input("점수를 입력하세요: "))
if score>=90 and score<=100:
    print("A")
elif score>=80 and score<90:
    print("B")
elif score>=70 and score<60:
    print("C")
elif score >= 60 and score < 70:
    print("D")
elif score>=50 and score<60:
    print("E")
else:
    print("잘못된 점수")
score=None
if score:
    print(none)
else:
    print("0을 입력하셨습니다.")

switcher={
    0:'일요일',
    1:'월요일',
    2:'화요일',
    3:'수요일',
    4:'목요일',
    5:'금요일',
    6:'토요일'
}
print(switcher.get(3, "알 수 없는 요일"))'''

x=9
y= False if x<10 else True
print(y)