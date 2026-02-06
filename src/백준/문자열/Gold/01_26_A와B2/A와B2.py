import sys
input=sys.stdin.readline
S=input().strip()
T=input().strip()

def dfs(T):
    if len(T)==len(S):
        if T==S:
            print(1)
            exit()
        elif T!=S:
            return
    if T[-1]=="A":
        new_a=T[:-1]
        dfs(new_a)
    if T[0]=="B":
        new_b=T[1:]
        new_b=new_b[::-1]
        dfs(new_b)

dfs(T)
print(0)

# import sys
# input = sys.stdin.readline
#
# S = input().strip()
# T = input().strip()
#
# def dfs(t):
#     # 1. 종료 조건: 길이가 같아졌을 때
#     if len(t) == len(S):
#         return t == S  # 같으면 True, 다르면 False 반환
#
#     # 2. 가지치기 & 재귀 호출
#
#     # Case A: 맨 뒤가 'A'라면 -> 떼고 재귀
#     if t[-1] == 'A':
#         if dfs(t[:-1]): # A를 뗀 문자열을 넘김
#             return True
#
#     # Case B: 맨 앞이 'B'라면 -> 떼고 뒤집어서 재귀
#     if t[0] == 'B':
#         # t[1:] (B 떼기) -> [::-1] (뒤집기)
#         if dfs(t[1:][::-1]):
#             return True
#
#     return False # 둘 다 안 되면 False
#
# # 실행
# if dfs(T):
#     print(1)
# else:
#     print(0)