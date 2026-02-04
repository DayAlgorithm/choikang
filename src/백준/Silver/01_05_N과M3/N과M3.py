import sys

n,m=map(int,sys.stdin.readline().split())
rs=[]

def dfs(index,count):
    if count==m:
        print(*rs)
        return
    for i in range(n):
        rs.append(i+1)
        dfs(i+1,count+1)
        rs.pop()

dfs(0,0)

