# import sys
# from collections import deque
#
# #m=가로=열, n=세로=행, h=높이
# m,n,h=map(int,input().split())
# # 이미 모두 익어있으면 0, 토마토가 모두 익지 못하면 -1, 나머지는 토마토가 전부 익는데 걸리는 날짜
# box=[[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
# rs=0
# q=deque()
#
# def bfs(height,row,col):
#     global rs
#     # 선 방문 시켜준다
#     box[height][row][col]=1
#     # 큐를 만들어준다
#     q=deque()
#     # 큐에 현재 위치를 넣어준다
#     q.append((height,row,col))
#     # 큐가 빌때까지 반복한다
#     while q:
#         h,r,c=q.popleft()
#
#         for dh,dr,dc in [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
#
#
#
#
# for i in range(h):
#     for j in range(n):
#         for k in range(m):
#             if box[i][j][k]==1:
#                 q.append((i,j,k))
#
