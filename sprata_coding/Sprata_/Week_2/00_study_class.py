class Person:
    def __init__(self, param_name):         # construcor 라는함수 -> 인자에 자기자신을 넘겨줘 파이썬 class 에선
        print("I am created", self)         # class 생성했을때 print 호출
        self.name = param_name              # class 내부 변수 self.name 에 param_name 저장.


    def talk(self):       # class 내부 함수는 method -> talk method를 만들었다. class Person에
                          # class 내부에 따른 함수
                          # self 는 항상 존재

        print("안녕하세요, 제 이름은",self.name,"입니다")

# 유사한 행동, 유사한 데이터 쉽게 쌓을 수 있음.
# 연관성 있는 데이터들을 클래스 내에서 관리 할 수 있으며, 다양한 객체 쉽게 생성 가능!

person_1 = Person("유재석")    # name = 유재석
print(person_1.name)
print(person_1)
person_1.talk()


person_2 = Person("박명수")    # name = 유재석
print(person_2.name)
print(person_2)
person_2.talk()