class Student:
    #클래스 속성 - 클래스에 1개만 생성
    auto_increment=0
    def __init__(self):
        Student.auto_increment+=1
        self.no=Student.auto_increment
    def __del__(self):
        print("인스턴스 소멸")

    @staticmethod
    def method():
        print("매개변수가 없는 static method")

Student.method()
'''stu1=Student()
print(stu1.no)
stu2=Student()
print(stu2.no)'''

stu1=Student() #인스턴스가 생성되고 참조 카운트가 1인 됨
stu1=None #참조를 가르키는 변수에 None을 대입하면 참조 카운트가 1 감소
#참조 카운트가 0이면 인스턴스가 소멸됨
print("프로그램 종료")

stu2=Student() #참조 카운트1
stu3=stu2  #다른 변수에 참조를 대입해서 참조 카운트는 1증가 -> 2
stu2=None #참조 카운트가 1 줄어들어도 1 - 인스턴스 소멸 안 됨
print("프로그램 종료")
