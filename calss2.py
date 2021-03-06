# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):  # __init__ : 생성자(객체)
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print('[지상 유닛 이동]')
        print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'.format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage): 
        Unit.__init__(self, name, hp, speed)   
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력{2}".format(self.name, location, self.damage))

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
        print("{0} : {1} 방향으로 날아갑니다. [속도{2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0 , damage) # 지상 스피드는 0   
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print('[공중 유닛 이동]')
        self.fly(self.name, location)
              
# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
# 매딕 : 의무병
# 드랍쉽 : 공중 유닛, 수송기. 마린/ 파이어뱃 / 탱크 등을 수송
# 벌쳐 : 지상 유닛, 기동성이 좋음 
vulture = AttackUnit('벌처', 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋고, 공격력도 좋음
battlecruiser = FlyableAttackUnit('배틀크루저', 500, 25, 3)
# 파이어뱃 : 공격 유닛, 화염방사기.

vulture.move('11시')
#battlecruiser.fly(battlecruiser.name, '9시')
battlecruiser.move('9시')

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

# marine1 = Unit("마린",40, 5)
# marine2 = Unit("마린",40, 5)
# tank1 = Unit("탱크",150, 35)
# firebat1 = Unit("파이어뱃", 50, 16)

# 레이스 : 공중 유닛, 비뱅기. 클로킹(상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (뻬앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))