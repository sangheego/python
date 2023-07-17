class DTO:
    def __init__(self,num=0, name='이름 없음'):
        self.__num=num
        self.__name=name

    @property
    def num(self):
        return self.__num
    @num.setter
    def name(self,num):
        return self.__name
    @num.setter
    def num(self,name):
        self.__name=name
    #인스턴스를 print함수에 대입했을 때 호출되는 메서드 - 오버라이딩
    #출력을 편리하기 위해서 재정의 - 디버깅 목적
    def __str__(self):
        return str(self.__num)+":"+self.__name

dto1=DTO(1,'nancy')
dto2=DTO(2,'grace')
data=[dto1,dto2]

import pickle
try:
    with open("./new.txt",'wb')as f:
        #f에 데이터를 serializable
        pickle.dump(data,f)
except Exception as e:
    print(e)

try:
    with open("./new.txt",'rb')as f:
        #f에 저장된 내용을 Deserializable
        result=pickle.load(f)
        for dto in result:
            print(dto)
except Exception as e:
    print(e)