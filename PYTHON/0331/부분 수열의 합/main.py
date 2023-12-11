import sys
sys.stdin = open('sample_input.txt')


# 백트래킹 : 가능 한 모든 경우 => 답 (시간 초과 有, 복잡도 미리 검토)
# 1. 종료 조건 (n) , n : 숫자 번호(index)
# 2. tree (시각적) n == N 일때 종료
# dfs(n, sum,
    # if n == N: # 종료 조건(n관련)
        # if sum == K : ans += 1
        # return
# dfs(n+1, sum + list[n]    # 포함 o
# dfs(n+1, sum)             # 포함 x

def dfs(n, sum_v):
    global ans
    # 3. 가지치기 : 더이상 정답 갱신 가능성이 없는 경우
    # 가장 마지막에, 가장 위쪽에
    if K < sum_v:
        return

    # 1. 종료 조건(n에 관련) : 반드시 정답 처리는 이곳에서만 !
    if n == N:
        if sum_v == K:
            ans += 1
        return
    # 2. 하부 호출
    dfs(n+1, sum_v + A[n])  # 포함
    dfs(n+1, sum_v)         # 포함 x

    
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    dfs(0, 0)

    print(f'#{tc} {ans}')

