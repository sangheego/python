#dict를 이용한 mvc
#dto 역할을 수행하는 클래스 생성 - 최근에는 더 권장
class DTO:
    def __init__(self,name="noname",tel='전화없음'):
        self.name=name
        self.tel=tel

datas=[DTO('adam','010'),DTO('jessica','011')]

for data in datas:
    print(data.name,data.tel)

#이차원 배열 대신에 dict 사용
'''kia=['a','b']
lg=['c','d']

kbo=[kia,lg]  #리스트의 리스트
#리스트는 인덱스를 이용해서 접근하고 dict는 key를 이용해서 접근
#enumerate는 인덱스와 데이터를 튜플로 리턴
for idx, baseball in enumerate(kbo):
    if idx==0:
        print("기아", end="\t")
    else:
        print("엘지",end="\t")
    for player in baseball:
        print(player, end="\t")
    print()'''

kia=['a','b']
lg=['c','d']
hanhwa=['e']

kbo=[{'team':'기아','data':kia},{'team':'엘지','data':lg},{'team':'한화','data':hanhwa}]
for dic in kbo:
    print(dic.get('team'), end=":")
    for player in dic.get("data"):
        print(player, end="\t")
    print()