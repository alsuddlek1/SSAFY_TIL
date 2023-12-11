# 배열, 왼쪽, 오른쪽
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

nums = [11, 45, 23, 81, 20, 34]
quick_sort(nums, 0, len(nums)-1)
print(nums)