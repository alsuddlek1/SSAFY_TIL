import sys
sys.stdin = open('input.txt')

# 가능한 모든 경우 n: 직원 번호(index)

def dfs(n, sm):
    global ans
    # 이미 만점일 때
    if ans == 0:
        return
    # 최소값 가지치기
    if ans <= sm-B:
        return
    if n == N :
        if sm >= B:
            ans = min(ans, sm-B)
        return

    dfs(n+1, sm+lst[n])     # 포함
    dfs(n+1, sm)            # 안포함

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = N*10000
    dfs(0, 0)

    print(f'#{tc} {ans}')