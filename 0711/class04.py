'''class Student:
    def __init__(self, name="noname"):
        self.__name=name  #속성 이름이 __로 시작하므로 인스턴스로 접근 불가
    #접근자 메서드
    @property #getter 설정
    def getName(self):
        print("name의 getter 호출")
        return self.__name
    @name.setter
    def name(self,name):
        print("name의 setter 호출")
        self.__name=name

    #프로퍼티 생성
    name=property(fget=getName,fset=setName)
stu=Student()
#setter와 getter를 직접 호출
stu.setName("파이터")
print(stu.getName())
#property를 이용한 getter와 setter호출
stu.name="나이트"
print(stu.name)'''

class Student:
    def __init__(self, name="noname"):
        self.name=name
    #+연산자 오버로딩
    def __add__(self, other):
        return self.name + other.name
    #+=연산자 오버로딩
    def __eq__(self, other):
        return self.name==other.name
stu1=Student("a")
stu2=Student("a")
print(stu1+stu2)

print(stu1==stu2)
print(stu1 is stu2)
