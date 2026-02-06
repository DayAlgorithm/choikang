import sys
input=sys.stdin.readline

S=list(input().strip())
T=list(input().strip())

def dfs(t):
    #기저조건
    if len(t)==len(S):
        if S==t:
            print(1)
            exit()
        elif S!=t:
            return
    #매개변수T
    #슬라이싱은 복사해서 쓴다는점을 생각해야함
    if t[-1]=="A":
        dfs(t[:-1])
        # A_t=t[:-1]
        # dfs(A_t)
        # A_t=A_t.append("A")
    if t[0]=="B":
        dfs(t[1:][::-1])
        # B_t=t[1:]
        # B_t=B_t[::-1]
        # dfs(B_t)
        # B_t=B_t[::-1]
        # t=B_t.append("B")
dfs(T)
#dfs를 돌아도 1이 아니라 아무것도 안되고 함수가 return 됐다면 0을 출력
print(0)