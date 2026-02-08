import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    l_stack=[]
    r_stack=[]
    s=input().strip()

    for char in s:
        # <
        # b< , <b
        if char=="<":
            if l_stack:
                r_stack.append(l_stack.pop())
        # >
        elif char==">":
            if r_stack:
                l_stack.append(r_stack.pop())
        # -
        elif char=="-":
            if l_stack:
                l_stack.pop()
        # 문자
        else:
            l_stack.append(char)

    rs=l_stack+r_stack[::-1]
    print("".join(rs))