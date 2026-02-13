import sys
input=sys.stdin.readline
boards=[[0]*101 for _ in range(101)]

t=int(input())
count=0
for _ in range(t):
    x,y=map(int,input().split())

    for i in range(x,x+10):
        for j in range(y,y+10):
            boards[i][j]=1

for i in range(101):
    for j in range(101):
        if boards[i][j]==1:
            count+=1

print(count)