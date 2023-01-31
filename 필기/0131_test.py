# def emoji_decorator(func):
#     def wrapper(name):
#         func(name)
#         print('^~^//')

#     return wrapper # wrapper라는 함수를 return

# @emoji_decorator
# def ko_hello(name):
#     print(f'안녕하세요, {name}님!')
#     # print('^~^//')

# @emoji_decorator
# def en_hello(name):
#     print(f'Hello, {name}!')

# def add_emoji(name, func):
#     func(name)
# #     print('^~^//')

# ko_hello('aiden') #ko_hello 라는 함수를 실행만 했지만, 데코레이션에 의해 실행


# # new_func = emoji_decorator(ko_hello)
# # new_func('aiden')
# # =>

# emoji_decorator(ko_hello)('aiden')
# emoji_decorator(en_hello)('aiden')

# add_emoji('aiden', ko_hello) 
# add_emoji('aiden', en_hello)

# # ko_hello('aiden')
# # en_hello('aiden')

# class MyClass:

#     def method(self):
#         return 'instance method', self

#     @classmethod
#     def classmethod(cls):
#         return 'class method',cls

#     @staticmethod
#     def staticmethod():
#         return 'static method'

# my_class = MyClass()
# print(my_class.method)
# print(my_class.classmethod)
# print(my_class.staticmethod)


class Person:
    def __init__(self):
        self.age = 0

    @property
    def age(self):      # getter
        print('getter 호출 !')
        return self._age

    @age.setter
    def age(self, age): # setter
        print('setter 호출')
        self._age = age

    # age = property(get_age, set_age) 

# ///

p1 = Person()
# p1._age = 25  # 이거안됨!
# print(p1._age) # 이것두 안됨

# 불편행 ,,
# p1.set_age(25)
# print(p1.get_age())

p1.age = 25
print(p1.age) # 왜 나는 setter가 두번 호출되지