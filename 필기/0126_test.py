# cafe = ['starbucks', 'tomntoms', 'hollys']

# print(cafe.insert(0, 'start'))

# # 문자열이 주어지면 숫자, 문자, 기호가 몇개인지 출력하는 함수

# def check(input_str):
#     char_count = 0
#     digit_count = 0
#     symbol_count = 0

#     for char in input_str:
#         if char.isalpha():
#             char_count += 1
#         elif char.isdigit():
#             digit_count += 1
#         else:
#             symbol_count += 1

#     return char_count, digit_count, symbol_count

# input_str = "123#$!aiden_snow"
# char_count, digit_count, symbol_count = check(input_str)
# print(f"char:{char_count}, digit : {digit_count}, symbol : {symbol_count}")

# ## 
# sample_list = [11, 22, 33, 55, 66]

# # 주어진 리스트의 4번째 자리(3번 인덱스)에 있는 항목을 제거하고 변수에 할당해 주세요.

# print("original list", sample_list)

# elem = sample_list.pop(3)

# print('list after: ', sample_list)
# print('elem : ', elem)

# # sample_list 의 가장 뒤에 77를 추가해보세요
# sample_list.append(77)

# # 할당해놓은 변수의 값을 sample_list의 2번 index에 추가해보세요
# print(sample_list)
# sample_list.insert(2, elem)
# print(sample_list)


# ##

# my_tuple = (11, 22, 33, 44, 55, 66)

# # 주어진 튜플에서 44와 55의 값을 새로운 튜플에할당해보세요
# new_tuple = my_tuple[3:5]
# print(new_tuple)

a = [1,2,3]
b = a

b[0] = 0
print(a)
print(b)

a = [1,2,3]
b = a.copy()

b[0] = 0
print(a)
# >>> [1,2,3]
print(b)
# >>>[0,2,3]