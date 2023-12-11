import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = len(arr)

    # 원소 N개의 모든 경우의 수
    # 2**N 은 1 << N 과 같다
    # 원소의 개수가 3개라고 할때
    # 2 ** 3 == 8
    # 1 << 3 -> 0b1000 -> 8
    # 0001 -> 1을 왼쪽으로 3번 밀면
    # 1000
    # print(8>>3)
    for i in range(1<<N): # N = len(10개의 정수)
        result = 0
        # i -> N 으로 만들 수 있는 모든 경우의 수
        # i 번째부터 2**n번째 의 경우의 수
        for j in range(N): # 모든 요소의 개수
            if i & (1<<j):
                # print(arr[j])
                result + arr[j]
        if result == 0:
            print(i)
            break
    else: # break 한번도 안했으면 else
        print(0)
        # print()

