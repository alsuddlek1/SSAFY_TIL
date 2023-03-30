# 백트래킹 N-Queen 2806

def promising(i, j):
    for di, dj in [[-1, -1], [-1, 0], [-1, 1]]:
        ni, nj = i + di, j + dj
        while 0 <= ni < N and 0 <= nj < N:
            if board[ni][nj]:   # 다른 퀸이 있으면
                return 0        # 실패
            ni, nj = ni + di, nj + dj
    return 1        # i, j에 놓을 수 있음

def f(i, N):
    global cnt
    if i == N: # N개의 퀸을 놓은 경우
        cnt += 1
    else:
        for j in range(N):
            if promising(i,j):
                board[i][j] = 1
                f(i+1, N)
                board[i][j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    board = [[0]*N for _ in range(N)]
    cnt = 0
    f(0, N)
    # print(f'#{tc} {cnt}')


# 연습문제 2
# {1,2,3,4,5,6,7,8,9,10}의 powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오

# 이건 머임?
def f(i,k, s, key):
    global cnt
    global c
    c += 1
    if i == k:
        if s == key:
            print(bit)
            cnt += 1
    else:
        bit[i] = 0
        f(i+1, k, s, key)   # A[i] 미포함
        bit[i] = 1
        f(i+1, k, s+A[i], key) # A[i] 포함

A = [i for i in range(1, 11)]
N = 10
bit = [0]*N
key = 1
cnt = 0
c = 0 # 재귀 호출 횟수
f(0, N, 0, key)
# print(cnt, c)

# 백트래킹
def f(i,k, s, key):
    global cnt
    global c
    c += 1

    if s == key:
        cnt += 1
        return
    elif i == k or s > key:
        return
    else:
        bit[i] = 0
        f(i+1, k, s, key)   # A[i] 미포함
        bit[i] = 1
        f(i+1, k, s+A[i], key) # A[i] 포함

A = [i for i in range(1, 11)]
N = 10
bit = [0]*N
key = 55
cnt = 0
c = 0 # 재귀 호출 횟수
f(0, N, 0, key)
# print(cnt, c)

# 뭐하는거징
def f(i,k, s, key, rs):
    global cnt
    global c
    c += 1

    if s == key:
        cnt += 1
        return
    elif i == k or s > key or s + rs < key:
        return
    else:
        bit[i] = 0
        f(i+1, k, s, key, rs - A[i])   # A[i] 미포함
        bit[i] = 1
        f(i+1, k, s+A[i], key, rs - A[i]) # A[i] 포함

A = [i for i in range(1, 11)]
N = 10
bit = [0]*N
key = 55
cnt = 0
c = 0 # 재귀 호출 횟수
f(0, N, 0, key, sum(A))
print(cnt, c)

