grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

# print(grain_lst.sort()) # None 반환
# print(grain_lst) # 정렬한 리스트확인

# grain_dict = dict(grain_lst)
# key = list(grain_dict.keys())
# value = list(grain_dict.values())
# print(value.index(max(value))) # 2

# max_idx = value.index(max(value))
# print(key[max_idx])

grain_lst.sort(key=lambda x : x[1],reverse=True)
print(grain_lst[0][0])