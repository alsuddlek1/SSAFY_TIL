'''
문제
개의 속성과 행위를 정의하는 Doggy 클래스를 만들어라. 

구성 요소
i.   초기화 메서드는 인자로 개의 이름과 견종을 받아서 인스턴스 변수에 할당한다.
ii.  bark() 메서드를 호출하면 개는 짖을 수 있다.
iii. 클래스 변수는 태어난 개의 숫자와 현재 있는 개의 숫자를 기록하는 변수로 구성한다.
        개가 태어나면 num_of_dogs와 birth_of_dogs의 값이 각 1씩 증가한다.
        개가 죽으면 num_of_dogs의 값이 1 감소한다.
iv.  get_status() 메서드를 호출하면 birth_of_dogs와 num_of_dogs의 수를 출력할 수 있다 
'''

class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Doggy.num_of_dogs += 1  # self.num_of_dogs => instance 변수가 되어버린다.
        Doggy.birth_of_dogs += 1
    
    def bark(self):
        return '왈왈!'

    @classmethod
    def get_status(cls):
        return f'누적 마리수 :{cls.birth_of_dogs}, 생존해 있는 마리 수 : {cls.num_of_dogs}'

    def __del__(self):
        Doggy.num_of_dogs -= 1
        print('안녕..')

# print(Doggy.num_of_dogs, Doggy.birth_of_dogs)
print(Doggy.get_status())
choco = Doggy('초코','푸들')
# print(Doggy.num_of_dogs, Doggy.birth_of_dogs)
print(Doggy.get_status())

del choco
print(Doggy.get_status())

poppy = Doggy('뽀삐', '말티즈')
del poppy

print(Doggy.get_status())
# print('instance로 classmethod 접근 및 호출 가능')
# print(choco.get_status())
# print(type(choco), isinstance(choco, Doggy))