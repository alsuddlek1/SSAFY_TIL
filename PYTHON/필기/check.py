# TOOLS 로 부터 뭔가 가져와 ~~

from calc import tools

print(tools.add(1, 2))
print(tools.sub(3, 4))

from calc.tools import add, sub

print(add(1,2))
print(sub(3,4))