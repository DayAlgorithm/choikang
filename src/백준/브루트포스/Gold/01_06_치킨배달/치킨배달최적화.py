import sys

# 빠른 입력을 위해 사용
input = sys.stdin.readline

N, M = map(int, input().split())

houses = []
chickens = []

# 1. 지도 전체를 돌며 집과 치킨집 좌표만 추출
for r in range(N):
    row = list(map(int, input().split()))
    for c in range(N):
        if row[c] == 1:
            houses.append((r, c))
        elif row[c] == 2:
            chickens.append((r, c))

# [최적화 핵심] 모든 집과 모든 치킨집 사이의 거리를 미리 계산해둠 (표 만들기)
# dist_table[h][c] = h번째 집과 c번째 치킨집 사이의 거리
# 이렇게 하면 나중에 뺄셈 계산 없이 표에서 숫자만 쏙 꺼내오면 됨
dist_table = []
for hr, hc in houses:
    temp = []
    for cr, cc in chickens:
        dist = abs(hr - cr) + abs(hc - cc)
        temp.append(dist)
    dist_table.append(temp)

result = float('inf')
selected_indices = [] # 내가 선택한 치킨집의 '번호(index)'를 저장

def dfs(idx, count):
    global result

    # [종료 조건] M개를 모두 골랐을 때 -> 거리 계산 시작
    if count == M:
        current_city_chicken_dist = 0

        # 모든 집에 대하여 (미리 만든 표를 보고 최소 거리 찾기)
        for h in range(len(houses)):
            min_dist_for_house = float('inf')

            # 내가 선택한 치킨집들 중에서 가장 가까운 거리 찾기
            for c_idx in selected_indices:
                # 계산(abs) 안 하고 표에서 값만 가져옴 -> 속도 UP
                dist = dist_table[h][c_idx]

                # 최솟값 갱신
                if dist < min_dist_for_house:
                    min_dist_for_house = dist

            current_city_chicken_dist += min_dist_for_house

            # [가지치기] 이미 현재 최솟값(result)을 넘어버렸다면 중단 (더 볼 필요 없음)
            if current_city_chicken_dist >= result:
                return

        # 최종적으로 더 작으면 결과 갱신
        if current_city_chicken_dist < result:
            result = current_city_chicken_dist
        return

    # [백트래킹] idx부터 치킨집 하나씩 골라보기
    for i in range(idx, len(chickens)):
        selected_indices.append(i) # 치킨집 번호 담기
        dfs(i + 1, count + 1)      # 다음 거 고르러 가기
        selected_indices.pop()     # 다녀와서 빼기 (원상복구)

# 0번 치킨집부터 시작, 현재 0개 선택함
dfs(0, 0)

print(result)