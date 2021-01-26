# Class # 상속

# 일반 유닛 / 오버라이딩!
class Unit:  # 부모클래스
    def __init__(self, name, hp, speed):  # 객체,
        self.name = name  # 멤버변수 class 내에서 정의된 변수!
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다.[속도 {2}]".format(self.name, location, self.speed))


# 공격 유닛 / Method / 다중 상속 -> 부모가 2이상이야!
class AttackUnit(Unit):  # 공격유닛은 Unit을 상속받아서 만들어진거야! // 자식클래스
    def __init__(self, name, hp, speed, damage):  # 객체
        Unit.__init__(self, name, hp, speed)  # 상속을 받았어!
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))


# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):  # 다중상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 스피드는 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


#  발키리 : 공중 공격 유닛
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

#   Unit                    Flyable
#   [move()]                  []
#    |                         |
#  Attack Unit    ㅡ   FlyableAttackUnit
# [Marine, Tank]       [move(), Wraith]

# # 벌쳐 : 지상 유닛
# vulture = AttackUnit("벌쳐", 80, 10, 20)
# vulture.move("11시")
#
# # 배틀크루저 : 공중 공격 유닛
# battlecruiser = FlyableAttackUnit("배틀크루져", 500, 25, 3)
# battlecruiser.move("9시")

'''pass !!! super!!!'''


# 빌딩
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):  # pass  아무것도 안하고 넘어가자!
        super().Unit.__init__(name, hp, 0)  # Super 를 통해서 init // 1. 괄호쳐주고 2. self 없앤다!
        self.location = location

