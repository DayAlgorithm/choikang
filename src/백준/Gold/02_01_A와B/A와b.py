import sys
sys.setrecursionlimit(2000)
input=sys.stdin.readline
# ABBA - ABB - BA - B
# 뒤에 삭제니까 스택써도 됨
S=input().strip()
T=input().strip()

#슬라이싱해서 바로 다음 함수로 보내면 복사된 값을 보낸다
def solution(T):
    if len(T)==len(S):
        if T==S:
            print(1)
            exit()
        else:
            print(0)
            exit()
    if T[-1]=="A":
        solution(T[:-1])
    elif T[-1]=="B":
        solution(T[:-1][::-1])

solution(T)
