import sys
input=sys.stdin.readline
from collections import deque

T=int(input())
for _ in range(T):
    p=input().strip()
    n=int(input())
    str=input().strip()

    if n==0:
        q=deque()
    else:
        q=deque(str[1:-1].split(","))

    is_reverse=False
    is_error=False

    for i in p:
        if i=="R":
            is_reverse=not is_reverse
        elif i=="D":
            if not q:
                is_error=True
                break
            if is_reverse:
                q.pop()
            else:
                q.popleft()

    if is_error:
        print("error")
    else:
        if is_reverse:
            q.reverse()
        print("["+",".join(q)+"]")