import sys

input=sys.stdin.readline

# 상하좌우
dr=[-1,1,0,0]
dc=[0,0,-1,1]
count=0

def dfs(r,c):
    board[r][c]=0

    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]

        if 0<=nr<n and 0<=nc<m and board[nr][nc]==1:
            board[nr][nc]=0
            dfs(nr,nc)

t=int(input())
for _ in range(t):
    # m=가로 n=세로 k=배추가 심어진 위치의 갯수
    m,n,k=map(int,input().split())
    # 0으로 이루어 진 2차원 배열 땅 생성
    board=list([0]*m for _ in range(n))

    # 배추 심어주기
    for _ in range(k):
        # x=열 y=행
        x,y=map(int,input().split())
        board[y][x]=1

    count=0
    # 이중 for문 말고 한칸씩 계속 이동하면서 dfs 검사해주기
    for i in range(n*m):
        # 행
        r=i//m
        # 열
        c=i%m
        if board[r][c]==1:
            dfs(r,c)
            count+=1
    print(count)

