import sys

n, m = map(int, sys.stdin.readline().split())
rs = []

# [변경 1] 0번부터 n-1번 인덱스를 쓸 거니까 크기는 n이면 충분합니다.
checked = [False] * n

def recursive(num):
    if num == m:
        print(*rs)
        return

    # [변경 2] range(n) -> 0, 1, 2, ..., n-1 까지 돕니다.
    for i in range(n):

        # checked[0], checked[1]... 을 검사합니다.
        if checked[i] == False:
            checked[i] = True

            # [변경 3] i는 0이지만, 문제에서 원하는 숫자는 1이어야 하죠?
            # 그래서 넣을 때만 1을 더해서 넣어줍니다.
            rs.append(i + 1)

            recursive(num + 1)

            checked[i] = False
            rs.pop()

recursive(0)


# import sys
#
# # 입력 받기
# N, M = map(int, sys.stdin.readline().split())
#
# rs = []          # 결과를 담을 리스트 (스택 역할)
# chk = [False] * (N + 1) # 방문 여부 체크 (1~N 인덱스 사용)
#
# def recur(num):
#     # [1] 종료 조건: M개를 모두 골랐으면 출력
#     if num == M:
#         print(' '.join(map(str, rs))) # [1, 2] -> "1 2" 출력
#         return
#
#     # [2] 1부터 N까지 반복
#     for i in range(1, N + 1):
#         if chk[i] == False: # 아직 안 쓴 숫자라면
#             chk[i] = True   # 1. 방문 표시 (찜하기)
#             rs.append(i)    # 2. 결과 리스트에 넣기
#
#             recur(num + 1)  # 3. 다음 숫자 고르러 더 깊이 들어감 (재귀)
#
#             # [3] 백트래킹 (가장 중요한 부분!)
#             # 재귀에서 돌아왔다는 건 i를 포함한 모든 경우를 다 봤다는 뜻
#             chk[i] = False  # 4. 방문 표시 해제 (다음에 쓰기 위해)
#             rs.pop()        # 5. 결과 리스트에서 빼기 (원상복구)
#
# # 함수 시작 (0개 고른 상태에서 출발)
# recur(0)
