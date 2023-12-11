import sys
sys.stdin = open('sample_input.txt')

# 출발지는 1번, 마지막에 1로 복귀

def dfs(n ,sm, cur):
    global ans
    if n == N-1:
        # 여태까지의 소모량 +1 번으로 복귀비용
        ans = min(ans, sm+arr[cur][0])
        return

    if ans <= sm:
        return

    for j in range(1, N):
        if visited[j] == 0:
            visited[j] = 1
            dfs(n+1, sm+arr[cur][j], j)
            visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 100*N
    visited = [0]*N

    dfs(0, 0, 0)
    print(f'#{tc} {ans}')