import sys
sys.stdin = open('sample_input.txt')

def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt +=1
    result = []
    l, r = 0, 0
    while len(left) > l or len(right) > r:
        if len(left) > l and len(right) > r:
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        elif len(left) > l:
            result.append(left[l])
            l += 1
        elif len(right) > r:
            result.append(right[r])
            r += 1
    return result


# msort(arr) 일때
def msort(m):
    if len(m) == 1:
        return m

    middle = len(m) // 2
    left = m[0 : middle]
    right = m[middle :]

    left = msort(left)
    right = msort(right)
    return merge(left, right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    res = msort(arr)
    # print(res)
    print(f'#{tc} {res[N // 2]} {cnt}')
