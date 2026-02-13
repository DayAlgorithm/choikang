import sys
input=sys.stdin.readline
#순서대로 북동남서
dr=[-1,0,1,0]
dc=[0,1,0,-1]

# n=행, m=열
n,m=map(int,input().split())
r,c,d=map(int,input().split())
#[[1,1,1],
# [1,0,1],
# [1,1,1]]
board=[list(map(int,input().split())) for _ in range(n)]
# 청소 칸 개수
count=0

def clean():
    global count,d,r,c,n,m

    while(True):
        if board[r][c]==0:
            board[r][c]=2
            count+=1

        # 진짜 중요한거 스캔과 이동을 같이 로직짜지 말기 분리하기
        is_blank=False
        # 4방향을 돌면서 빈칸이 있는지 없는지
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if 0<=nr<n and 0<=nc<m:
                if board[nr][nc]==0:
                    is_blank=True
                    break
        # 빈칸이 있다면 (청소할 곳이 있다면)
        if is_blank:
            d=(d+3)%4
            nr,nc=r+dr[d],c+dc[d]
            if board[nr][nc]==0:
                r,c=nr,nc
        else:
            nr,nc=r-dr[d],c-dc[d]
            if board[nr][nc]!=1:
                r,c=nr,nc
            else:
                break
clean()
print(count)

