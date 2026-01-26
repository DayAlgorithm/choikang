import sys
from collections import deque
input=sys.stdin.readline
while(True):
    C,R=map(int,input().split())
    board=[list(map(int,input().split())) for _ in range(R)]

    if C==0 and R==0:
        break

    def bfs(r,c):
        q=deque()
        board[r][c]=0
        q.append((r,c))
        while q:
            qr,qc=q.popleft()
            for dr,dc in [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]:
                nr,nc=qr+dr,qc+dc
                if 0<=nr<R and 0<=nc<C:
                    if board[nr][nc]==1:
                        board[nr][nc]=0
                        q.append((nr,nc))
    count=0
    for i in range(R):
        for j in range(C):
            if board[i][j]==1:
                bfs(i,j)
                count+=1
    print(count)