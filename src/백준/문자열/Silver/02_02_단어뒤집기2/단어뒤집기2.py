import sys
input=sys.stdin.readline

S=input().strip()
stack=[]
rs=[]
is_tag=False

for char in S:
    if char=="<":
        is_tag=True
        while stack:
            rs.append(stack.pop())
        rs.append(char)
    elif char==">":
        is_tag=False
        rs.append(char)
    elif is_tag:
        rs.append(char)
    elif not is_tag:
        # 태그 밖인데 공백이라면
        if char==" ":
            while stack:
                rs.append(stack.pop())
            rs.append(char)
        elif char.isalnum():
            stack.append(char)
while stack:
    rs.append(stack.pop())

print("".join(rs))



