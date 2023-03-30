import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())        # N : 컨테이너수 , M : 트럭 수
    W = list(map(int, input().split()))     # N개의 화물의 무게
    T = list(map(int, input().split()))     # M개의 트럭 적재용량

    W.sort()    # N개의 화물 무게를 오름차순 정렬
    T.sort()    # M개의 트럭 적재용량 오름차순 정렬
    result = 0  # 옮겨진 화물 전체 무게

    while T and W:      # 이동할 화물이 없을 때 까지
        A = W.pop()     # 화물 중 가장 큰 값
        B = T.pop()     # 적재용량 중 가장 큰 값

        if B >= A:  # 적재 용량이 화물보다 값이 크거나 같을 때 운반 가능 하므로
            result += A     # 운반 가능한 무게 +

        else:
            T.append(B)     # 그 다음으로 큰 화물과 비교하기 위하여 다시 append

    print(f'#{tc}', result)