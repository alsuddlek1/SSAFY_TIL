

entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']


# # entry_record에 등장한 횟수 ... 를 각 사람마다 기록
# # -> 각각 고유한 사람마다 특정한 value 를 가지고 있어야한다.

# entry_count_dict = {}
# for name in entry_record:
#     # if entry_count_dict[name]
#     entry_count_dict[name] = entry_count_dict.get(name, 0) +1
# print(entry_count_dict)

# print("입장 기록이 가장 많은 TOP 3")
# print(sorted(entry_count_dict.items(),
#             key=lambda item: item[1],
#             reverse=True
#             )[:3])

# exit_count_dict = {name : 0 for name in set(exit_record)}
# for name in exit_record:
#     entry_count_dict[name] += 1
# print(exit_count_dict)

# for name, count in entry_count_dict.items():
#     print(name, count)
#     print(exit_count_dict[name])
#     print('='*30)
#     diff = count - exit_count_dict[name]
#     print(diff)
#     if diff > 0:
#         print(f'{name}은 입장기록이 {diff}번 더 입장했습니다.')
#     elif diff < 0:
#         print(f'{name}은 퇴장기록이 {-diff}번 더 입장했습니다.')

from collections import Counter

a = Counter(entry_record)
b = Counter(exit_record)

print(a,b)
a.subtract(b)
print(a)