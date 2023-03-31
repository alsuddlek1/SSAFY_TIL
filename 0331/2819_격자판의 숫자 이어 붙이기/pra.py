import sys
sys.stdin = open('sample_input.txt')

dx = [-1, 1, 0, 0] # 상,하,좌,우
dy = [0, 0, -1, 1]

def dfs(n, A , x, y):
    if n == 7:
        return

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    # 중복제거

    for x in range(4):
        for y in range(4):
            A = arr[x][y]

    res = [0]*7


