import sys

n=int(sys.stdin.readline())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
rs=float("inf")
visited=[False]*n

def dfs(index,count):
    global rs
    if count==(n//2):
        startSum=0
        linkSum=0

        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    startSum+=board[i][j]
                elif not visited[i] and not visited[j]:
                    linkSum+=board[i][j]

        rs=min(rs,abs(startSum-linkSum))
        return rs

    for i in range(index,n):
        if visited[i]==False:
            visited[i]=True
            dfs(i+1,count+1)
            visited[i]=False
dfs(0,0)
print(rs)


































# import sys
#
# # [1] 입력 받기
# input = sys.stdin.readline
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
#
# # [2] 방문 여부 체크 (True: 스타트팀, False: 링크팀)
# visited = [False] * N
# min_diff = float('inf') # 최솟값 저장용 (무한대로 초기화)
#
# def dfs(idx, count):
#     global min_diff
#
#     # [3] 종료 조건: 팀원이 N/2명 모였을 때 (스타트 팀 완성)
#     if count == N // 2:
#         start_power = 0
#         link_power = 0
#
#         # [4] 능력치 계산 (2중 for문)
#         # 전체 인원(N)을 돌면서 팀을 구분해 점수를 더함
#         for i in range(N):
#             for j in range(N):
#                 # 두 명 다 True면 -> 스타트 팀 시너지
#                 if visited[i] and visited[j]:
#                     start_power += board[i][j]
#                 # 두 명 다 False면 -> 링크 팀 시너지
#                 elif not visited[i] and not visited[j]:
#                     link_power += board[i][j]
#
#         # [5] 차이의 최솟값 갱신
#         min_diff = min(min_diff, abs(start_power - link_power))
#         return
#
#     # [6] 백트래킹 (조합 만들기: N과 M 2번 로직)
#     # idx부터 시작하여 중복 방지 & 오름차순 유지 (순서 없는 조합)
#     for i in range(idx, N):
#         if not visited[i]:
#             visited[i] = True   # 스타트 팀 영입
#             dfs(i + 1, count + 1)
#             visited[i] = False  # 방출 (백트래킹)
#
# # 실행 (0번 사람부터 탐색 시작)
# dfs(0, 0)
# print(min_diff)