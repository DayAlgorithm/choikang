import sys
from collections import deque
input=sys.stdin.readline
m,n,h=map(int,input().split()) # 가로,세로,높이
box=[[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
max_day=0
q=deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k]==1:
                q.append((i,j,k))

def bfs():
    global min_day
    while q:
        qh,qr,qc=q.popleft()
        for dh,dr,dc in [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
            nh,nr,nc=qh+dh,qr+dr,qc+dc
            if 0<=nh<h and 0<=nr<n and 0<=nc<m:
                if box[nh][nr][nc]==0:
                    box[nh][nr][nc]=box[qh][qr][qc]+1
                    q.append((nh,nr,nc))

bfs()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k]==0:
                print(-1)
                exit()

            max_day=max(max_day,box[i][j][k])
print(max_day-1)