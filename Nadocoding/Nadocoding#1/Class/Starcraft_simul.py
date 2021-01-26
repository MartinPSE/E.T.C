# Class # 상속

# 일반 유닛 / 오버라이딩!
from random import *


class Unit:  # 부모클래스
    def __init__(self, name, hp, speed):  # 객체,
        self.name = name  # 멤버변수 class 내에서 정의된 변수!
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):

        print("{0} : {1} 방향으로 이동합니다.[속도 {2}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 공격 유닛 / Method / 다중 상속 -> 부모가 2이상이야!
class AttackUnit(Unit):  # 공격유닛은 Unit을 상속받아서 만들어진거야! // 자식클래스
    def __init__(self, name, hp, speed, damage):  # 객체
        Unit.__init__(self, name, hp, speed)  # 상속을 받았어!
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]".format(self.name, location, self.damage))


class Marine(AttackUnit):  # 스팀팩 있어!
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


class Tank(AttackUnit):  # 시즈모드!
    seize_developed = False  # 시즈모드 O ? X ?

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        # 현재 시즈모드가 아니고 -> 시즈모드로 전환
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드일때 -> 시즈모드를 해제
        else:
            print("{0} : 시즈모드로 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


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

        self.fly(self.name, location)


class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False  # 클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocked == True:  # 클로킹 모드 -> 모드 해제
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False

        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")


# 게임 시작
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 생성

t1 = Tank()
t2 = Tank()

# 레이스
w1 = Wraith()

# 유닛 일괄 관리
attack_units = [m1, m2, m3, t1, t2, w1]

# 가자 !!

for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.set_seize_mode(True)
print("알림 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 ( 탱크 : 시즈모드, 레이스 : 클로킹, 마린 : 스팀팩)
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 공격!!
for unit in attack_units:
    unit.attack("1시")

# 피해를 입어
for unit in attack_units:
    unit.damaged(randint(5, 21))  # 공격을 랜덤으로 받아보자 ( 5 ~ 20 )

# 전군이 죽으면
game_over()
