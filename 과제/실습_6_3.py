# count_vowels('apple') #=> 2
# count_vowels('banana') #=> 3

def count_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    # vowels = 'aeiou' 라고 해도 됨
    result = 0
    for v in word:
        if v in vowels:
             result += 1
    return result


## 풀이
# def count_vowels(words):
#     vowels = 'aeiou'
#     result = 0

#     for vowels in words:
#         for char in words:
#             if char == vowels:
#                 result += 1
#     return result

## 메서드 풀이

# def count_vowels(words):
#     vowels = 'aeiou'
#     result = 0

#     for vowel in vowels:
#         result += words.count(vowel)
#     return result



print(count_vowels('apple')) #=> 2
print(count_vowels('banana')) #=> 3