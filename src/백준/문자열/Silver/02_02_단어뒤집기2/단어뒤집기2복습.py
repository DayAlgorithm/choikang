import sys
input=sys.stdin.readline
s=input().strip()
rs=[]
stack=[]
is_tag=False

for char in s:
    # <,>," ",태그 밖,태그 안,
    if char==" ":
        while stack:
            rs.append(stack.pop())
        rs.append(char)
    elif char=="<":
        is_tag=True
        while stack:
            rs.append(stack.pop())
        rs.append(char)
    elif char==">":
        is_tag=False
        rs.append(char)
    else:
        if is_tag:
            rs.append(char)
        else:
            stack.append(char)

while stack:
    rs.append(stack.pop())

print("".join(rs))





