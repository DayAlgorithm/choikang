import sys
from collections import deque
input=sys.stdin.readline

def bfs(r,c):
    q=deque()
    # board 리스트를 함수 안에서 사용할 수 있는지 궁금
    board[r][c]=0
    q.append((r,c))

    while q:
        qr,qc=q.popleft()
        for dr,dc in [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,-1],[-1,1]]:
            nr,nc=qr+dr,qc+dc
            if 0<=nr<H and 0<=nc<W:
                if board[nr][nc]==1:
                    board[nr][nc]=0
                    q.append((nr,nc))

while(True):
    W,H=map(int,input().split())
    board=[list(map(int,input().split())) for _ in range(H)]

    if W==0 and H==0:
        break

    count=0

    for i in range(H):
        for j in range(W):
            if board[i][j]==1:
                bfs(i,j)
                count+=1
    print(count)