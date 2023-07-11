import abc

class AbstractClass(metaclass=abc.ABCMeta):
    #추상 메서드 - 내용이 없는 메서드로 하위 클래스에서 구현해서 사용해야 함
    @abc.abstractmethod
    def method(self):
        pass
class_Sub(AbstractClass):
    def __init__(self):
        print("인스턴스 생성")
    #추상클래스를 상속 받을 떄는 추상 메서드를 반드시 implementation해주어야 함
    def method(self):
        print('추상 메서드 구현')
instance = Sub()
#instance = AbstractClss()
#추상 클래스는 인스턴스를 만들 수 없어서 에러