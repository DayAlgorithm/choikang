import sys
input=sys.stdin.readline
n,m=map(int,input().split())
board=[list(input().strip())for _ in range(n)]
max_value=-1e9
visited=[0]*26

def dfs(r,c,count):
    global max_value
    max_value=max(max_value,count)
    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr,nc=r+dr,c+dc
        if 0<=nr<n and 0<=nc<m:
            cal_index=ord(board[nr][nc])-ord("A")
            if visited[cal_index]==False:
                visited[cal_index]=True
                dfs(nr,nc,count+1)
                visited[cal_index]=False

first=ord(board[0][0])-ord("A")
visited[first]=True
dfs(0,0,1)
print(max_value)