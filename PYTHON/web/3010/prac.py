import sys
sys.stdin = open('input.txt')

N, M = map(int,input().split())
data = []
result = []
for _ in range(1,N+1):
    result.append(_)
    data.append(_)
# print(data)
# for x in range(M):
i, j = map(int, input().split())
result[j-1] = data[i-1]
result[i-1] = data[j-1]
print(result)