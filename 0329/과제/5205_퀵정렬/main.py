import sys
sys.stdin = open('sample_input.txt')

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#         left, right = [], []
#         for i in range(1, len(arr)):
#             if arr[i] > pivot:
#                 right.append((arr[i]))
#             else:
#                 left.append(arr[i])
#         return [*quick_sort(left), pivot, *quick_sort(right)]

def quick_sort(arr, left, right):
    if left < right:
        mid = cal(arr, left, right)
        quick_sort(arr, left, mid-1)
        quick_sort(arr, mid+1, right)

def cal(arr, left, right): # left, right : 인덱스
    # 피벗보다 큰 구간의 왼쪽 경계
    i = left - 1
    # 피벗보다 큰 구간의 오른쪽 경계
    j = left
    # lomuto 분할 방식은 가장 오른쪽 원소를 피봇으로 결정
    pivot = arr[right]
    while j < right:
        if pivot > arr[j]:
            i += 1
            # i 와 j가 서로 다른 위치에 있다면
            # i와 j 사이 구간에 피봇보다 큰 값이 있다.
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr)-1)

    # print(res)
    # result = res[N // 2]
    print(f'#{tc} {arr[N//2]}')
    # print(f'#{tc} {result}')