# 600,000개 , 길이 100,000
# 커서는 문장의 맨 앞, 문장의 맨 뒤, 문장 중간에 위치 가능
import sys
input=sys.stdin.readline

n=input().strip()
m=int(input())
#문자열을 리스트로 감싸면 문자를 쪼개서 string_list로 만들어줌
l_stack=list(n)
r_stack=[]

for _ in range(m):
    # split("") 사용법 익히기
    order=input().split()
    if order[0]=="L":
       if l_stack:
           r_stack.append(l_stack.pop())
    elif order[0]=="D":
        if r_stack:
            l_stack.append(r_stack.pop())
    elif order[0]=="B":
        if l_stack:
            l_stack.pop()
    elif order[0]=="P" and order[1].isalnum:
        l_stack.append(order[1])

print("".join(l_stack)+"".join(r_stack[::-1]))






