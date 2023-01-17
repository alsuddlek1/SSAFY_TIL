# 해(year)가 4의 배수이면서 100의 배수가 아니면 윤년
year = int(input('해를 입력하시오 : '))

if year % 4 == 0 and year % 100 != 0:
    print('윤년1')
else:
    print('윤년아님')
# 400의 배수이면 윤년
if year % 400 == 0:
    print('윤년2')
else:
    print('윤년아님')
# 위 두 조건 중 하나라도 맞으면 윤년