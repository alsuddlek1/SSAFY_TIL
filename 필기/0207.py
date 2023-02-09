# 이진검색

def binarySearch(a, N, key):
    # key : 내가 찾으려고 하는 값
    # N : 최대 개수
    # a : 전체,,그 뭐라그러냐 그거
    start = 0
    end = N-1
    while start <= end: # 검색구간이 남아 있으면
        middle = (start + end)//2
        if a[middle] == key : # 검색성공
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle +1
    return  False

## 재귀 함수

def binarySearch2(a, start, end, key):
    if start > end:
        return False
    else:
        middle = (start + end)//2
        if a[middle] == key:
            return True
        elif a[middle] > key:
            return binarySearch2(a, start, middle-1, key)
        else:
            return binarySearch2(a, middle+1, end, key)

## 선택 정렬

def selectionSort(a, N):
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if a[minIdx] > a[j]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]

'''
7
7 2 5 3 4 6 4
'''

## 크키순으로 정렬(선택정렬)
N = int(input())
arr = list(map(int,input().split()))

for i in range(N-1):    # 작업 구간의 시작 인덱스
    minIdx = i          # 맨 앞이 최소라 가정하자
    for j in range(i+1, N):
        if arr[minIdx] > arr[j]:
            minIdx = j
    arr[minIdx], arr[i] = arr[i], arr[minIdx]

print(arr)

## k번째로 작은 원소 찾기

def select(arr, k):
    for a in range(0, k):
        minIndex = a
        for b in range(a+1, len(arr)):
            if arr[minIndex] > arr[b]:
                minIndex = b
        arr[a], arr[minIndex] = arr[minIndex],arr[a]
    return arr[k-1]