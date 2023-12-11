import sys
sys.stdin = open('sample_input.txt')

def dfs(n, sum_v):
    # n : arr index
    if sum_v > K:
        return

    global ans
    if n == N:
        if sum_v == K:
            ans += 1
        return

    dfs(n+1, sum_v + arr[n])
    dfs(n+1, sum_v)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) # N : N개의 자연수, K : N개의 자연수의 합
    arr = list(map(int, input().split()))

    ans = 0
    dfs(0, 0)
    print(f'#{tc} {ans}')