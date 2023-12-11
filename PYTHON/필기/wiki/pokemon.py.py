# 의뢰를 받았다
# 푸키먼이라는 게임을 만들어 달라
# 푸키먼이란... 가상 세계의 동물들이 있는데,
# 각각 고유의 lv, hp, skill, info 을 가진 생명체 들이다.
# 이 생명체들은 둘이 만나게 되면 싸우게 되는데 한명의 hp가 0이 될때까지 싸운다

# 공통 속성을 가진 객체를 정의
# 클래스명 정의 할때는 ClassName -> Pascal Case
# -> 단어 기준으로 앞글자를 대문자로

class Pokemon:
    # 모든 푸키먼들이 공통으로 가지는 속성
    # 클래스 변수
    info = '푸키먼...'
    population = 0

    # 생성자
    # 매직 매서드 -> __name__
    # 인스턴스 매서드 -> 첫번째 인자는 자기 자신
    # 함수 정의하는 것과 동일하다 -> 모든 규칙이 똑같이 작동
    def __init__(self, name, lv=1):
        # classmethod 인 increase 호출
        Pokemon.increase()

        # 인스턴스 변수에 생성될 때 넘겨받은 이름을할당
        self.name = name
        self.lv = lv
        # 스킬 명과, 공격력
        self.skill = ('몸통 박치기', 10)
        self.hp = 100

        # 본인만의 독특한 소개법
        self.info = self.name[:2] * 2

    # 행동을 정의 해 보자.
    def attack(self):       # instance
        print(f'{self.info}')
        return self.skill[1] # 공격력

    @classmethod
    def increase(cls):       # mathod
        cls.population += 1

    # 첫번째 인자로 self, cls 둘다 받지 않는다.
    @staticmethod
    def battle(pok1, pok2): # 함수 정의와 동일하다.
        # 영원히 
        while True:
            pok2.hp -= pok1.attack()
            if pok2.hp <= 0:
                print(f'{pok2.name}이 쓰러졌다!!')
                return

            pok1.hp -= pok2.attack()
            if pok1.hp <= 0:
                print(f'{pok1.name}이 쓰러졌다!!')
                return

# pika == Pokemon 의 인스턴스
# 생성자에는 2개의 인자를 넣어주기로 했다.
# lv은 기본 값이 있어서 이름만 넣어도 된다.
print(Pokemon.population, '피카츄가 태어나기 전')
pika = Pokemon('피카츄') # 새로운 객체를 생성하여 pika에 할당

print(Pokemon.population, '피카츄가 태어나고 난 후')
print(pika.name)
print(pika.lv, pika.skill, pika.hp)
print(pika.info) # info = class 속성
pika.attack()

# 똑같이 Pokemon에 해당하는 새로운 객체를 생성
meta = Pokemon('메타몽', 5)
print(meta.name)
print(meta.lv, meta.skill, meta.hp)
print(meta.info) # 푸키먼...
meta.attack()

Pokemon.battle(pika, meta)



# print(pika.population) # 접근해서 출력은 가능한데...

# pika.population += 1
# print(pika.population)      # 1
# print(Pokemon.population)   # 0

# 강제로 increase 를 호출해서 인구수를 늘려보자
# print('----실험중-----')
# # Pokemon.increase()
# pika.increase() # classmethod가 아니라면?
# print(Pokemon.population)
# print(pika.population)