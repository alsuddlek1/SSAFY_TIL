# while i < N               # 텍스트를 벗어나지 않기
# #
# #     if t[i] == p[j]:
# #         i += 1
# #         j += 1
# #
# #     else:
# #         i = i-j+1
# #         j = 0

p = "is" # 찾을 패턴
t = "This is a book~!" # 전체 텍스트
M = len(p)
N = len(t)

def BruteForce(p,t,N,M):
    i = 0 # t에서의 비교위치
    j = 0 # p 에서의 비교위치
    while j < M and i < N : # 비교할 문장이 남아있고, 패턴을 찾기 전이면
        if t[i] == p[j]:       # 서로 같은 글자를 만나면(방법2)
            i += 1
            j += 1
        else:
            i = i - j +1
            j = 0
        # if t[i] != p[j]:    # 서로 다른 글자를 만나면 (방법1)
        #     i = i - j       # 비교를 시작한 위치로
        #     j = -1          # 패턴 시작 전으로
        # i = i + 1
        # j = j + 1
    if j == M : # 패턴을 찾은 경우
        return i -M
    else :
        return  -1
#패턴의위치
def bf2(p, t, N, M):
    for i in range(N-M+1):
        for j in range(M):
            if t[i+j] != p[j]:
                break
        else:
            return i
    return -1
# print(bf2(p,t,N,M))

#패턴의 개수 (왜 안되징)
def bf3(p, t, N, M):
    cnt = 0
    for i in range(N-M+1):
        for j in range(M):
            if t[i+j] != p[j]:
                break
        else:
            cnt += 1
            # return i
    return cnt
# print(bf2(p,t,N,M))

### KMP 알고리즘
