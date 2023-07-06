year= 2023
#윤년: 4의 배수이고 100의 배수 아닌 경우 or
# 400의 배수인 경우
if year %4==0 & year%100 !=0 | year%400==0: #앞에 확률이 더 놓은 걸 적는다
    print(year,"은 윤년")
else:
    print(year,"은 윤년이 아님")



