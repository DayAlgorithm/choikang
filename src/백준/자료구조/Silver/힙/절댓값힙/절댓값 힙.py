import sys
import heapq
input=sys.stdin.readline

n=int(input())
rs=[]
for _ in range(n):
    v=int(input())

    if v!=0:
        heapq.heappush(rs,(abs(v),v))
    else:
        if rs:
           print(heapq.heappop(rs)[1])
        else:
            print(0)
