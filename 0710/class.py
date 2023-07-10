'''class Student:
    def disp(self):
        print("인스턴스 생성")
    def setName(self, name):
        self.name=name #self.name은 인스턴스의 속성으로 만들어짐
#인스턴스 생성
student=Student()
#메서드 호출 - bound 호출
student.disp()
#메서드 호출 - unbound 호출
Student.disp(student)
class Student:
    class_data="클래스의 속성"
student=Student()
print(Student.class_data) #클래스 이름을 이용해서 클래스 속성에 접근
print(student.class_data) #인스턴스 이름을 이용해서 클래스 속성에 접근

Student.class_data="클래스 데이터 수정"
print(Student.class_data) #클래스 이름을 이용해서 클래스 속성에 접근
print(student.class_data) #인스턴스 이름을 이용해서 클래스 속성에 접근

student.class_data="인스턴스 이용해서 클래스 데이터 수정"
print(Student.class_data) #클래스 이름을 이용해서 클래스 속성에 접근
print(student.class_data) #인스턴스 이름을 이용해서 클래스 속성에 접근'''

class Student:
    class_data="클래스의 속성"
#인스턴스 생성해서 대입
stu1=Student()
#인스턴스 생성해서 대입
stu2=Student()
#stu1의 데이터를 대입: stu1이 참조하고 있는 데이터의 참조를 stu3가 참조
stu3=stu1
#2개의 인스턴스가 동일한지 여부 확인
print(stu1==stu2)#내부의 데이터가 같은지 확인
print(stu1 is stu2) #id가 같은지 확인
print(stu1==stu3)
print(stu1 is stu3)

#이름과 점수를 갖는 객체를 여러 개 필요
class Student:
    def getName(self):
        return self.name
    def setName(self,name):
        self.name=name
    def getScore(self):
        return self.score
    def setScore(self,score):
        self.score=score
stu1=Student()
#setter를 이용한 속성 생성과 설정
stu1.setName("nancy")
stu1.setScore(100)
#getter를 이용한 속성 사용
print(stu1.getName())
print(stu1.getScore())