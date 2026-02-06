import sys
import heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())

    min_heap = []
    max_heap = []
    # k+1이 아니라 k여도 0~k-1까지 쓰므로 충분 (단, 문제 범위 체크 필요)
    # 여기선 i가 0부터 k-1까지니까 [0]*k로 충분함
    visited = [False] * k

    for i in range(k):
        cmd, n = input().split()
        n = int(n)

        if cmd == "I":
            # [수정 1] 중요! (값, ID) 순서여야 값이 정렬 기준이 됨
            # 님의 코드는 (i, -n)이라서 i(순서)대로 정렬되어버림
            heapq.heappush(max_heap, (-n, i))
            heapq.heappush(min_heap, (n, i))
            visited[i] = True
        else:
            if n == 1:
                # [수정 2] max_heap[0]은 (-값, ID) 튜플임. ID는 [1]에 있음
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False # 사망 신고
                    heapq.heappop(max_heap)
            else:
                # [수정 2] min_heap[0]은 (값, ID) 튜플임. ID는 [1]에 있음
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False # 사망 신고
                    heapq.heappop(min_heap)

    # [수정 3] 마지막 청소 (여기도 오타 수정)
    # visited[0][0] 아님! 현재 힙의 top에 있는 ID를 봐야 함
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    # [수정 4] 논리 조건 수정
    # 하나라도 비어있으면 EMPTY가 아니라, 둘 다 비어있을 때 EMPTY여야 함
    # (위에서 청소했으니 둘 중 하나만 비어있을 수는 없음. 둘 다 비거나 둘 다 있거나)
    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        # max_heap은 -값으로 저장했으니 다시 - 붙여서 출력
        print(-max_heap[0][0], min_heap[0][0])













import sys
import heapq

input = sys.stdin.readline

# 테스트 케이스 개수
T = int(input())

for _ in range(T):
    k = int(input())

    # 1. 두 개의 힙과 생존 신고 장부(visited) 준비
    min_heap = []
    max_heap = []

    # visited[i] -> i번째 입력된 숫자가 살아있는지(True) 죽었는지(False) 체크
    # k가 최대 100만이니 넉넉하게 잡음
    visited = [False] * k

    for i in range(k):
        cmd, num = input().split()
        num = int(num)

        if cmd == 'I':
            # 2. 삽입: (값, ID) 형태로 저장
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i)) # 최대힙엔 부호 반대로!
            visited[i] = True # i번째 놈 살아있다 신고

        else: # cmd == 'D'
            if num == 1: # 최댓값 삭제
                # 3. 청소(동기화): 이미 죽은 유령들은 걷어냄
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)

                # 4. 진짜 삭제
                if max_heap:
                    visited[max_heap[0][1]] = False # 장부에 사망 신고
                    heapq.heappop(max_heap)

            else: # 최솟값 삭제
                # 3. 청소(동기화)
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)

                # 4. 진짜 삭제
                if min_heap:
                    visited[min_heap[0][1]] = False # 장부에 사망 신고
                    heapq.heappop(min_heap)

    # 5. 최종 청소: 연산이 다 끝나고도 유령이 남아있을 수 있음
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    # 6. 결과 출력
    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        # max_heap[0][0]은 -가 붙어있으니 다시 -를 붙여서 양수로 복구
        print(-max_heap[0][0], min_heap[0][0])