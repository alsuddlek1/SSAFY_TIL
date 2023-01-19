def my_magic_func(n):
    return n * 10

my_list = [1, 2, 3, 4, 5]

map_obj = map(my_magic_func, my_list)
print(list(map_obj))

# zip
name_list = ['신동민', '서재현', '박영서', '이태성', '정예원', '이은석']
age_list = [17, 18, 22, 24, 25, 19]

for each in zip(name_list, age_list):
    print(each)

for name, age in zip(name_list, age_list):
    print(name,age)

# lambda
rlt = (lambda x: x * x)(4)
print(rlt)

my_func = lambda n : n * 2
print(my_func(2))

map_obj = map(lambda n : n * 10, [1,2,3])
rlt = list(map_obj)
print(rlt)

# 재귀함수

# def recur():
#     print('뿅!')
#     recur()

# recur()

def fac(n):
    if n == 0: # 재귀 그만두는 부분 꼭!! 넣기 ~ 맨날 오늘 3분만 더쓰면 도대체 언제 13분 쉬어
        return 1
    return n * fac(n - 1)
# 시작은 5부터했지만, 0부터 시작함(?)
print(fac(5))

# 패킹 / 언패킹  *

# x, y = 1,2
# z = 1, 2, 3


def my_func(x, y, *z): # def my_func(x, y, *z, a) 이거 안돼! 왜냐면 z가 이미 다 빨아먹음
    return x + y + z #=> 갯수 안맞음 : 이때 가변인자

numbers = [1,2,3,4]
my_func(*numbers)

a, *b = 1, 2, 3, 4
# 파이썬아~ 하나 넣고 남는거 b에 다 넣어주라
print(a, b) # 1 [2, 3, 4]

def my_sum(a, b, c):
    return a + b + c

num_list = [10, 20, 30]

# rlt = my_sum(num_list[0], num_list[1], num_list[2])
rlt = my_sum(*num_list) # 덩어리 앞에 * 붙어있으면 언패킹 (곱하기 아님)

def test(*values):
    for value in values:
        print(value)

test(1)
test(1, 2)
test(1, 2, 3, 4)

def my_sum(a, b, *agrs):
    rlt = 0
    for value in agrs:
        rlt += value
    return rlt

# my_sum() #0
# my_sum(1, 2, 3) #6

def test(**kwargs):
    print(kwargs, type(kwargs))
    return kwargs

test(name = 'aiden', age = 21)

# import random
from random import shuffle

