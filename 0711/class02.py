class Student:
    #def disp(self):
    def __init__(self):
        print("인스턴스 메서드")
        #만들어져가는 클래스에 만들어졌지만 인스턴스 없이는 호출할 수 없는 메서드
    #setter - 속성을 수정하거나 생성하는 메서드
    def setName(self,name):
        self.name=name #name이라는 속성이 없으면 만들어서 대입하고 존재하면 수정
    #getter - 속성의 값을 사용할 수 있도록 리턴하는 메서드
    def getName(self):
        return self.name

stu1=Student() #인스턴스 생성
#메서드 호출
Student.disp(stu1) #인스턴스의 메서드를 호출 - unbound 호출
stu1.disp() #self에 인스턴스가 대입돼서 메서드를 호출 - bound 호출

stu1.setName("nancy")
print(stu1.getName())