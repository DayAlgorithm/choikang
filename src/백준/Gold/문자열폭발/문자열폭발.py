import sys
input=sys.stdin.readline

str_list=input().strip()
boom_list=list(input().strip())

stack=[]
boom_len=len(boom_list)

for i in str_list:
    stack.append(i)
    if len(stack) >= boom_len:
       if stack[-boom_len:]==boom_list:
           del stack[-boom_len:]

if stack:
    print("".join(stack))
else:
    print("FRULA")