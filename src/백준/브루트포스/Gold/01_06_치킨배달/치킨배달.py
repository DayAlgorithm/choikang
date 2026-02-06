import sys

n,m = map(int,sys.stdin.readline().split())
city= [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

chickens=[]
selected_chickens=[]
houses=[]
answer=float("inf")

for r in range(n):
    for c in range(n):
        if city[r][c]==1:
            houses.append((r,c))
        elif city[r][c]==2:
            chickens.append((r,c))

def dfs(index,count):
    global answer
    if count==m:
        chicken_dist=0
        for hr,hc in houses:
            min_dist=float("inf")
            for cr,cc in selected_chickens:
                min_dist=min(min_dist,abs(hr-cr)+abs(hc-cc))
            chicken_dist+=min_dist
        answer=min(answer,chicken_dist)
        return

    for i in range(index,len(chickens)):
        selected_chickens.append(chickens[i])
        dfs(i+1,count+1)
        selected_chickens.pop()

dfs(0,0)
print(answer)




































# import sys
#
# # n과 m 입력받기
# n,m = int(sys.stdin.readline().split())
# # 도시 입력받기
# city = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# # 집과 치킨집 좌표를 담은 리스트 만들기
# houses = []
# chickens = []
# selected_chickens = []
# # city를 전체 탐색하면서 1로 표시된 곳은 houses에 추가 2로 표시된 곳은 chickens에 추가
# for r in range(n):
#     for c in range(n):
#         if city[r][c]==1:
#             houses.append((r,c))
#         elif city[r][c]==2:
#             chickens.append((r,c))
# # dfs 매개변수 현재 치킨집의 인덱스 종료조건 최대 m개
# def dfs(index,count):
#     if count==m:
#         total_dist=0
#         for hr,hc in houses:
#             min_dist=float('inf')
#             for cr,cc in selected_chickens:
#                 dist = abs(hr-cr) + abs(hc-cc)
#                 min_dist = min(min_dist,dist) #영수집에서 치킨집 a와b중 더 거리가 최소인 값
#             total_dist+=min_dist
#         return total_dist
# # 종료조건 m개가 되었다면 집에서 치킨집까지의 최소 거리를 구하고 각 집의 최소거리를 모두 더했을때의 최소
# # 종료조건 m이 안되었다면 치킨집의 인덱스를 하나 더해주고 현재 치킨집 개수 +1




















# import sys
#
# N, M = map(int, sys.stdin.readline().split())
# city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#
# houses = []
# chickens = []
#
# # 1. 집과 치킨집 좌표 수집
# for r in range(N):
#     for c in range(N):
#         if city[r][c] == 1:
#             houses.append((r, c))
#         elif city[r][c] == 2:
#             chickens.append((r, c))
#
# # 정답(최솟값) 저장 변수
# result = float('inf')
#
# # 선택된 치킨집들을 담을 리스트 (N과 M에서의 'rs' 역할)
# selected_chickens = []
#
# # ==========================================
# # 여기가 바로 [백트래킹] 파트입니다! ⭐
# # ==========================================
# def dfs(idx, count):
#     global result
#
#     # [종료 조건] M개를 다 골랐다면? (M개 폐업 안 시키고 살림)
#     if count == M:
#         # 이 조합으로 도시의 치킨 거리 계산 (완전 탐색)
#         total_dist = 0
#         for hr, hc in houses:
#             min_dist = float('inf')
#             for cr, cc in selected_chickens:
#                 dist = abs(hr - cr) + abs(hc - cc)
#                 min_dist = min(min_dist, dist)
#             total_dist += min_dist
#
#             # (가지치기: 이미 최솟값 넘어가면 중단)
#             if total_dist >= result:
#                 return
#
#                 # 최솟값 갱신
#         result = min(result, total_dist)
#         return
#
#     # [재귀 호출] 현재 위치(idx)부터 끝까지 하나씩 골라봄
#     for i in range(idx, len(chickens)):
#         # 1. 치킨집 선택 (바구니에 담기)
#         selected_chickens.append(chickens[i])
#
#         # 2. 다음 치킨집 고르러 가기 (깊이 + 1)
#         dfs(i + 1, count + 1)
#
#         # 3. 백트래킹 (다녀와서 바구니에서 빼기 - 원상복구) 🔙
#         selected_chickens.pop()
#
# # 백트래킹 시작 (0번 인덱스부터, 현재 0개 선택됨)
# dfs(0, 0)
#
# print(result)
#
