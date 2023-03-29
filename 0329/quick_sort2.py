def quick_sort(arr):
    # 분할정복
    if len(arr) <= 1:
        return arr
    else:
        # 분할작업
        pivot = arr[0]
        left, right = [], []
        for i in range(1, len(arr)):
            if arr[i] > pivot:
                right.append(arr[i])
            else:
                left.append(arr[i])
        return [*quick_sort(left), pivot, *quick_sort(right)]

nums = [55, 45, 23, 81, 28, 60]
quick_sort(nums, 0, len(nums)-1)