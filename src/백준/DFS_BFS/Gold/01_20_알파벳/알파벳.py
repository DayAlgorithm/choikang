import sys

# r,c 입력받기
R,C=map(int,sys.stdin.readline().split())
# board[][] 리스트
board=[list(sys.stdin.readline().strip()) for _ in range(R)]
# 검증
# print(" \n".join(map(str,board)))
# 알파벳 visited 배열 선언 26개
visited=[False]*26
max_value=-1e9
# 상하좌우 좌표
dr=[1,-1,0,0]
dc=[0,0,1,-1]

def dfs(r,c,count):
    global max_value
    # 기저조건은 따로 없음
    max_value=max(max_value,count)
    # r,c 상하좌우 이동했을때의 경우
    for i in range(4):
        nr,nc= r+dr[i],c+dc[i]
        # 맵 밖으로 나가면 continue 가지마라
        if not (0<=nr<R and 0<=nc<C):
            continue
        alpha=ord(board[nr][nc])-65
        # 이미 방문했으면 continue 즉 가지마라
        if visited[alpha]:
            continue
        visited[alpha]=True
        dfs(nr,nc,count+1)
        visited[alpha]=False

start=ord(board[0][0])-65
visited[start]=True
dfs(0,0,1)
print(max_value)
