import sys
sys.stdin = open('input.txt')

N, M = map(int,input().split())
data = []
result = []
for _ in range(1, N+1):
    data.append(_)
    result.append(_)
print(data)

for x in range(M):
    i, j = map(int, input().split())
    for y in range(j, i-1, -1):
        data[]