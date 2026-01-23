import sys
input=sys.stdin.readline

n,m=map(int,input().split())

listen=set()
for _ in range(n):
    listen.add(input().strip())
see=set()
for _ in range(m):
    see.add(input().strip())

listen_see=sorted(list((listen&see)))

print(len(listen_see))
print("\n".join(listen_see))


















# import sys
# input = sys.stdin.readline
#
# # 1. 입력 받기
# N, M = map(int, input().split())
#
# # 2. 듣도 못한 사람 -> Set으로 저장 (O(N))
# # 해시 테이블에 저장하므로 나중에 찾을 때 O(1)
# listen = set()
# for _ in range(N):
#     listen.add(input().strip())
#
# # 3. 보도 못한 사람 -> Set으로 저장 (O(M))
# see = set()
# for _ in range(M):
#     see.add(input().strip())
#
# # 4. 교집합(&) 구하고 사전순 정렬 (O(KlogK))
# # '&' 연산자가 내부적으로 최적화되어 있어서 매우 빠름
# result = sorted(list(listen & see))
#
# # 5. 출력
# print(len(result))
# for name in result:
#     print(name)