import sys
sys.setrecursionlimit(2000)
input=sys.stdin.readline

s=input().strip()
t=input().strip()

def solve(t):
    if len(t)<=len(s):
        if t==s:
            print(1)
            exit()
        else:
            return
    if t[-1]=="A":
        solve(t[:-1])
    else:
        solve(t[:-1][::-1])

solve(t)
print(0)