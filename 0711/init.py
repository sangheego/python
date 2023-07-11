class Student:
    #생성자 - 인스턴스를 생성할 때 호출하는 메서드
    #이 메서드에서 속성을 생성해서 속성을 처음부터 소유하도록 만들어주는 것이 좋음
    #매개변수를 이용해서 초기화하면 만들어질 때 다양한 값으로 초기화 가능
    #매개변수를 이용해서 초기화 할 때 매개변수에 기본값을 생성하지 않으면 인스턴스를 생성할 때 반드시 매개변수에 값을 대입해야 함
    def __init__(self, name="noname"):
        print("인스턴스 생성")
        #특정한 상수로 생성하고자 하는 경우는 생성자 내부에서 직접 설정
        #self.name="기본값"
        self.name=name
    #소멸자 - 인스턴스가 소멸될 때 호출되는 메서드
    def __del__(self):
        print("인스턴스 소멸")
    def setName(self,name):
        self.name=name #name이라는 속성이 없으면 만들어서 대입하고 존재하면 수정
    #getter - 속성의 값을 사용할 수 있도록 리턴하는 메서드
    def getName(self):
        return self.name
    #뒤에는 그대로.....?