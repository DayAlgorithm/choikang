import sys
block=[1,2,3,4]
print(block[1:])
print(max(block[1:]))




import sys

# 빠른 입력 (습관!)
input = sys.stdin.readline

# H: 세로, W: 가로
H, W = map(int, input().split())
blocks = list(map(int, input().split()))

total_water = 0

# 1. 양 끝(0번, W-1번)은 절대 물이 안 고임.
#    그러니 1번부터 W-2번까지만 검사하면 됨.
for i in range(1, W - 1):

    # [Left Max] 내 위치(i) 기준으로 왼쪽 벽들 중 가장 높은 벽 찾기
    left_max = max(blocks[:i])
    # [Right Max] 내 위치(i) 기준으로 오른쪽 벽들 중 가장 높은 벽 찾기
    right_max = max(blocks[i+1:])
    # [Water Level] 물은 두 대장 벽 중 '낮은 쪽' 높이만큼 참
    compare_wall = min(left_max, right_max)
    # [Calculate] 물 높이가 내 블록(blocks[i])보다 높아야 물이 고임
    if compare_wall > blocks[i]:
        total_water += compare_wall - blocks[i]

print(total_water)
