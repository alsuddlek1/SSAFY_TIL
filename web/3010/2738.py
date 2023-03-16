import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
matrix = [[0]*M for _ in range(N)]
for a in range(2):
    data = [list(map(int, input().split())) for _ in range(N)]
    # print(data)

    for i in range(N):
        for j in range(M):
            matrix[i][j] += data[i][j]

for i in matrix:
    print(*i)