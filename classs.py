from random import *

class unit :
    def __init__(self,name,hp,speed) : 
        self.name=name #self.name 등은 멤버변수라고 함
        self.hp=hp
        self.speed=speed
        print(f"{self.name}유닛이 생성되었습니다.")
    def move(self,location) :
        print(f"{self.name}유닛 {location}방향이동 :속도[{self.speed}]")


    def damaged(self,damage) :
       print(f"{self.name} : {damage}데미지를 입었습니다.")
       self.hp=self.hp-damage
       print(f"{self.name}의 남은체력 : {self.hp}")
       if self.hp <= 0 :
           print(f"{self.name}파괴되었습니다.")
    
      

class attackunit(unit) : #unit클래스를 상속받음
    def __init__(self,name,hp,speed,damage) : 
        unit.__init__(self,name,hp,speed)
        self.damage=damage

    def attack(self, location) :
        print(f"{self.name} : {location} 방향으로 공격합니다. 공격력 : {self.damage}")
     

class Flyable :
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self,name, location):
        print(f"{name} : {location}방향으로 날아갑니다. [속도:{self.flying_speed}]")


class Flyableattackunit(attackunit, Flyable) :
    def __init__(self,name,hp,damage,flying_speed) :
        attackunit.__init__(self,name,hp,0,damage) #지상스피드 : 0
        Flyable.__init__(self,flying_speed)
    def move(self,location) :
        self.fly(self.name,location)

class marine(attackunit) :
    def __init__(self) :
        attackunit.__init__(self,"마린",40,1,5)

    def stimpack(self) :
        if self.hp >10 :
            self.hp-=10 
            print(f"{self.name} : 스팀팩을 사용합니다. (HP 10감소)")
        else :
            print(f"{self.name}체력이 부족하여 스팀팩을 사용할 수 없습니다.")
    

class tank(attackunit) :
    seizemode_dev =False 
    def __init__(self) :
        attackunit.__init__(self,"탱크",150,1,35)
        self.seizemode = False

    def set_seizemode(self) :
        if tank.seizemode_dev==False :
            return
        if self.seizemode == False :
            print(f"{self.name}이 시즈모드로 전환합니다.")
            self.damage*=2
            self.seizemode=True
        else :
             print(f"{self.name}이 시즈모드를 해제합니다.")
             self.damage/=2
             self.seizemode=False

class wraith(Flyableattackunit) :
    def __init__(self) :
        Flyableattackunit.__init__(self,"레이스",80,20,5)
        self.clocked = False

    def clocking(self) :
        if self.clocked == True :
            print(f"{self.name}클로킹모드 해제합니다.")
            self.clocked =False
        else :
            print(f"{self.name}클로킹모드 설정합니다")
            self.clocked=True

def game_start():
    print("[알림] 게임이 시작되었습니다.")

def game_over() :
    print("Player : gg")
    print("[Player]님이 게임에서 퇴장하셨습니다.")
# wraith=unit("레이스",80,5)
# wraith2=unit("레이스2",80,5)
# wraith2.clocking=True #레이스2객체에 클로킹이라는 변수 추가할당

# if wraith2.clocking==True :
#     print(f"{wraith2.name}는 클로킹 상태입니다")


# firebat1 = attackunit("파이어뱃",50,16)
# firebat1.attack(1) 
# firebat1.damaged(50)

class buildingunit(unit):
    def __init__(self,name,hp,location) :
        unit.__init__(self,name,hp,0)#아래와같음
        super().__init__(name,hp,0)#위와같음 상속받은 부모클래스를 활용하는것임
        #pass #일단 클래스만들고 ㅇ ㅏ무것도 하지말라

# valkyrie=Flyableattackunit("발키리",200,6,5)
# valkyrie.fly(valkyrie.name, "3시")

# vulture.move(11)
# battle.fly("배틀크루져",9)  #매번 지상유닛인지 공중유닛인지 확인하고 함수써야함
# --> 연산자 오버라이딩으로 move함수만 사용


###실제 게임 진행
game_start()


m1=marine()
m2=marine()
m3=marine()

t1=tank()
t2=tank()

w1=wraith()

#유닛 일괄관리
attack_units=[]
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군이동
for u in attack_units :
    u.move("1시")

# 탱크 시즈모드 개발
tank.seizemode_dev = True
print("[알림] 탱크 시즈모드 개발완료")

#공격모드 준비 (마린은 스팀팩, 탱크시즈모드, 레이스 클로킹)
for u in attack_units :
    if isinstance(u, marine): #u각각 (마린3 탱크2 레이스1)이 어느 클래스의 인스턴스인지 확인
        u.stimpack()
    elif isinstance(u,tank):
        u.set_seizemode()
    elif isinstance(u,wraith):
        u.clocking()

#전군공격
for u in attack_units :
    u.attack("1시")

#전군피해
for u in attack_units :
    u.damaged(randint(5,21)) #5부터 21이내의 랜덤으로 피해

#게임 종료
game_over()
