import copy
import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())
map=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
max_value=-1e9

def bfs():
    global max_value
    # map을 건들면 안되니까 map의 복사본
    temp_map=copy.deepcopy(map)
    q=deque()
    # 바이러스를 조건에 따라 퍼트리기
    for r in range(n):
        for c in range(m):
            if temp_map[r][c]==2:
                q.append((r,c))
    #새로 bfs 시작하면 초기화
    while q:
        r,c = q.popleft()
        for dr,dc in [(1,0),(-1,0),(0,-1),(0,1)]:
            nr,nc=r+dr,c+dc
            #새로 이동한 위치가 범위 안에 들어오고, 벽에 붙이지 않는다면
            if 0<=nr<n and 0<=nc<m and temp_map[nr][nc]==0:
                temp_map[nr][nc]=2
                q.append((nr,nc))
    cnt=0
    for i in range(n):
        for j in range(m):
            if temp_map[i][j]==0:
                cnt+=1
    max_value=max(max_value,cnt)

def make_wall(index,count):
    # 기저조건
    if count==3:
        bfs()
        return

    # 0을 만나면 1로 바꿔주기
    for i in range(index,(n*m)):
        row=i//m
        col=i%m
        if map[row][col]==0:
            map[row][col]=1
            make_wall(i+1,count+1)
            map[row][col]=0

make_wall(0,0)
print(max_value)


























# import sys
# import copy
# from collections import deque
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# max_safe_area = 0
#
# # 바이러스 퍼뜨리기 (BFS) - 이건 기존과 동일
# def bfs():
#     global max_safe_area
#     # 벽이 세워진 상태의 board를 건드리면 안 되니 복사본 사용
#     temp_board = copy.deepcopy(board)
#     queue = deque()
#
#     # 바이러스 위치 찾기
#     for i in range(N):
#         for j in range(M):
#             if temp_board[i][j] == 2:
#                 queue.append((i, j))
#
#     while queue:
#         r, c = queue.popleft()
#         for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
#             nr, nc = r + dr, c + dc
#             if 0 <= nr < N and 0 <= nc < M:
#                 if temp_board[nr][nc] == 0:
#                     temp_board[nr][nc] = 2
#                     queue.append((nr, nc))
#
#     # 안전 영역 크기 계산
#     cnt = sum(row.count(0) for row in temp_board)
#     max_safe_area = max(max_safe_area, cnt)
#
# # [핵심] 벽 세우기 (백트래킹)
# # start: 이번 재귀에서 탐색을 시작할 1차원 인덱스 (중복 방지용)
# def make_wall(count, start):
#     # 1. 기저 조건: 벽 3개 다 세웠으면 바이러스 퍼뜨리기
#     if count == 3:
#         bfs()
#         return
#
#     # 2. start부터 끝까지 반복 (이전 위치는 안 봄 -> 조합)
#     for i in range(start, N * M):
#         r = i // M  # 행 계산
#         c = i % M   # 열 계산
#
#         if board[r][c] == 0:     # 빈 칸이라면
#             board[r][c] = 1      # [체크] 벽 세움 (visited = True 역할)
#
#             # 다음 재귀 호출 (벽 개수+1, 다음 인덱스 i+1 부터 탐색)
#             make_wall(count + 1, i + 1)
#
#             board[r][c] = 0      # [해제] 벽 허물기 (visited = False 역할)
#
# # 메인 실행
# make_wall(0, 0)
# print(max_safe_area)