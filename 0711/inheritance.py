class Sup:
    def superMethod(self):
        print("상위 클래스의 메서드")
class Sub(Sup):
    def subMethod(self):
        print("하위 클래스의 메서드")
#sub에 인스턴스 생성해서 필요한 메서드 호출
s=Sub()
s.subMethod()
s.superMethod() #sup상속 받아서 가능
