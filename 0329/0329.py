# def merge(left, right):
#     pass

# def msort(s, e):
#     ## msort(arr) 일때
#     # def msort(m):
#     # if len(m) == 1:
#     #     return m

#     # middle = len(m) // 2
#     # left = m[0 : middle]
#     # right = m[middle :]

#     # left = msort(left)
#     # right = msort(right)
#     # return merge(left, right)

#     if s == e:
#         return
#     m = (s+e) // 2
#     msort(s, m) # 인덱스
#     msort(m+1, e)
#     # merge
#     k = 0
#     l, r = s, m+1 # 왼쪽과 오른쪽에서 가장 작은 숫자의 위치
#     while l <= m or r <= e:
#         if l <= m and r <= e:
#             if arr[l] <= arr[r]:
#                 tmp[k] = arr[l]
#                 l += 1
#             else:
#                 tmp[k] = tmp[r]
#                 r += 1
#             k += 1
#         elif l <= m:
#             while l <= m:
#                 tmp[k] = arr[l]
#                 t += 1
#                 k += 1
#         elif r <= e:
#             while r <= e:
#                 tmp[k] = arr[r]
#     i = 0
#     while i < k:
#         arr[s+i] =tmp [i]
#     return merge()

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     tmp = [0] * N

#     # msort(arr)
#     msort(0, N-1)
#     print(arr)

def hoare(A, l, r):
    pivot = A[l] # 맨 왼쪽원소 기준
    i = l # pivot 보다 큰 값을 찾아 오른쪽으로 이동
    j = r # pivot 보다 작은 값을 찾아 왼쪽으로 이동

    while i <= j:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i < j: # 교차 하지 않은 경우
            A[i], A[j] = A[j], A[i]
    A[j], A[l] = A[l], A[j]
    return j

def qsort(A, l, r):
    if l < r:
        s = hoare(A, l, r)
        qsort(A, l, s-1)
        qsort(A, s+1, r)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    qsort = list(arr, 0, N-1)
    print(arr)