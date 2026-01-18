import sys
n=int(sys.stdin.readline())
board=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
min_value=1e9
visited=[False]*n
def dfs(index,count):
    global min_value
    if count==n//2:
        start=0
        link=0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start+=board[i][j]
                elif visited[i]==False and visited[j]==False:
                    link+=board[i][j]
        min_value=min(min_value,abs(start-link))
        return min_value

    for i in range(index,n):
        if visited[i]==False:
            visited[i]=True
            dfs(i+1,count+1)
            visited[i]=False

dfs(0,0)
print(min_value)