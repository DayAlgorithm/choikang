import sys
from collections import deque

m,n,k, = map(int, sys.stdin.readline().split())
graph = [[0]*n for _ in range(m)]

# for row in graph:
#     print(row)

for _ in range(k):
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            graph[y][x]=1

def bfs(y,x):
    q=deque([(y,x)])
    graph[y][x]=1
    size=1

    while q:
        cy,cx = q.popleft()
        for dy,dx in ([(0,-1),(0,1),(-1,0),(1,0)]):
            ny,nx = cy+dy, cx+dx
            if(0<=ny<m and 0<=nx<n and graph[ny][nx]==0):
                size+=1
                graph[ny][nx]=1
                q.append((ny,nx))
    return size

sol=[]
for y in range(m):
    for x in range(n):
        if(graph[y][x]==0):
            sol.append(bfs(y,x))

sol.sort()
print(len(sol))
print(*sol)


# import sys
# from collections import deque
#
# # 1. 입력 받기 (한 줄컷)
# m, n, k = map(int, sys.stdin.readline().split())
#
# # 2. 맵 생성 (리스트 컴프리헨션)
# graph = [[0] * n for _ in range(m)]
#
# # 3. 직사각형 그리기
# for _ in range(k):
#     x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
#     # 범위만큼 1로 채우기 (자바랑 똑같은 로직)
#     for y in range(y1, y2):
#         for x in range(x1, x2):
#             graph[y][x] = 1
#
# # 4. BFS 함수 정의
# def bfs(y, x):
#     q = deque([(y, x)])
#     graph[y][x] = 1 # 방문 처리
#     size = 1
#
#     while q:
#         cy, cx = q.popleft()
#         # 상하좌우 확인 (dx, dy 따로 안 만들고 튜플로 바로 처리 가능)
#         for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
#             ny, nx = cy + dy, cx + dx
#             if 0 <= ny < m and 0 <= nx < n and graph[ny][nx] == 0:
#                 graph[ny][nx] = 1 # 벽으로 메워버림
#                 size += 1
#                 q.append((ny, nx))
#     return size
#
# # 5. 전체 탐색 및 결과 출력
# areas = []
# for i in range(m):
#     for j in range(n):
#         if graph[i][j] == 0:
#             areas.append(bfs(i, j))
#
# areas.sort()
# print(len(areas))
# print(*areas) # 리스트의 모든 요소를 공백 두고 출력 (자바의 for문 대체)