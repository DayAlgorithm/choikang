import sys

n,m = map(int,sys.stdin.readline().split())

answer=[]

def dfs(depth,count):
    if count==m:
        print(*answer)
        return

    for i in range(depth,n):
        answer.append(i+1)
        dfs(i+1, count+1)
        answer.pop()

dfs(0,0)