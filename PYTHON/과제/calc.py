# 더하기
def add(a, b):
    # 함수가 하는 가장 중요한 역할
    # code block 작성된 특정한 로직을 '호출시마다' 실행하는데 있다.
    # 만약 그 결과를 반환해야 한다면,
    # return 뒤에는 표현식이 올 수 있고,
    # 반드시 하나의 객체만 반환하여야 하는데,
    # 만약 2개 이상의 개체를 반환하려고 한다면? -> 튜플로 묶어서 반환한다.
    return a + b

# 빼기
def sub(a, b):
    return a - b

# 곱하기
def mul(a, b):
    return a * b

#나누기
def div(a, b):
    result = 0
    error = '0으로 나눌수 없다.'
    try:
        result += a/b
        return result
    except:
        return error

# 함수 호출을 해보자.
# 정의한 함수이름 + (인자)
print(div(10, 0)) # a에는 10, b에는 0