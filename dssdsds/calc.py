def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b


def div(a, b):
    result = 0
    error = '0으로 나눌수 없다.'
    try:
        result += a/b
        return result
    except:
        return error
