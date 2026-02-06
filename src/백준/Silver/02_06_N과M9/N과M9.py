import sys
sys.setrecursionlimit(10**6)
from collections import Counter

input=sys.stdin.readline
n,m=map(int,input().split())
s=list(map(int,input().split()))

#({9: 2, 7: 1, 1: 1})
cnt=Counter(s)
# [1,7,9]
cnt_keys=sorted(cnt.keys())
rs=[]

def dfs(count):
    if count==m:
        print(*rs)
        return

    for i in cnt_keys:
        if cnt[i]>0:
            cnt[i]-=1
            rs.append(i)
            dfs(count+1)
            cnt[i]+=1
            rs.pop()

dfs(0)