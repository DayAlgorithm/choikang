import sys
input = sys.stdin.readline

n = int(input())
tops = list(map(int, input().split()))

stack = []
answer = [0] * n

# 1. 문법 수정: range(n) -> enumerate(tops)
for index, height in enumerate(tops):

    # 2. 로직 유지: 나보다 작은 애들 제거
    while stack and stack[-1][1] < height: # tops[index] 대신 height 쓰면 더 빠름
        stack.pop()

    # 3. 안전 장치 추가: if stack (스택이 비어있지 않은지 먼저 체크!)
    if stack:
        # 비어있지 않아야 stack[-1]을 볼 수 있음
        if stack[-1][1] > height:
            answer[index] = stack[-1][0]

    # 4. 내 정보 저장 (번호는 1부터 시작하니 index + 1)
    stack.append((index + 1, height))

print(" ".join(map(str, answer)))



















import sys
input = sys.stdin.readline

n = int(input())
# map 객체는 인덱싱이 안 되므로 list로 변환 필수!
towers = list(map(int, input().split()))

stack = []
answer = [0] * n

# ★ enumerate 사용! i는 0, 1, 2... height는 6, 9, 5... 로 자동 매핑됨
for i, height in enumerate(towers):

    # 1. 숙청 (나보다 작은 애들 방 빼)
    while stack and stack[-1][1] < height:
        stack.pop()

    # 2. 수신 (남은 애가 있으면 걔가 수신탑)
    if stack:
        # stack[-1][0]에는 이미 '1번부터 시작하는 번호'가 저장되어 있다고 가정
        answer[i] = stack[-1][0]

    # 3. 입장 (내 정보 저장)
    # ★ 중요: 나중에 남들이 내 번호를 쓸 때는 1번부터 셈해야 하므로 i+1을 저장
    stack.append((i + 1, height))

print(" ".join(map(str, answer)))