import sys

n,m=map(int,sys.stdin.readline().split())
rs=[]

def dfs(index,count):
    if m==count:
        print(*rs)
        return
    for i in range(index,n):
        rs.append(i+1)
        dfs(i,count+1)
        rs.pop()

dfs(0,0)