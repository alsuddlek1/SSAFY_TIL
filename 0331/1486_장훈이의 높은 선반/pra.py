import sys
sys.stdin = open('input.txt')

def dfs(n, sum_v):
    # n : 점원 s의 index


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split()) # N : 점원 수, B : 선반 높이
    S = list(map(int, input().split()))     # s : 점원들의 키

    ans = N*10000

    print(f'#{tc} {ans}')