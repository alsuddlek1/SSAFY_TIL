try:
    print(10/'우왕') 
    # 0으로 나누었다는 예외사황이 나옴
    # 0이 아닌 한글과 같은 예외상황도 '0안돼'가 출력됨
    # 0만 '0안돼'나오게 하려면 ZeroDivisionError
except ZeroDivisionError:
    print('0안돼')
except TypeError:
    print('정수 이외의 값으로 나눌 수 없습니다.')