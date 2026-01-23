import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 1. 리스트로 입력 받기
listen = [input().strip() for _ in range(N)]
see = [input().strip() for _ in range(M)]

# 2. 반드시 둘 다 정렬해야 함! (핵심) -> O(NlogN + MlogM)
listen.sort()
see.sort()

# 3. 투 포인터 탐색 -> O(N + M)
p1, p2 = 0, 0
result = []

while p1 < N and p2 < M:
    # Case 1: 두 이름이 같으면? -> 듣보잡 발견!
    if listen[p1] == see[p2]:
        result.append(listen[p1])
        p1 += 1
        p2 += 1

    # Case 2: listen 쪽 이름이 사전순으로 더 작으면?
    # 예: 'alice' vs 'bob' -> 'alice'는 절대 뒤에 나올 'bob'과 같을 수 없음
    # p1을 뒤로 한 칸 땡겨서 키워줘야 함
    elif listen[p1] < see[p2]:
        p1 += 1

    # Case 3: see 쪽 이름이 더 작으면?
    # p2를 뒤로 땡김
    else: # listen[p1] > see[p2]
        p2 += 1

# 4. 출력 (이미 정렬된 상태에서 찾았으므로 또 정렬할 필요 없음)
print(len(result))
for name in result:
    print(name)