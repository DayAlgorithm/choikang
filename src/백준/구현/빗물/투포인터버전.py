# 투 포인터 버전 (참고용)
left, right = 0, W - 1
left_max, right_max = blocks[left], blocks[right]
total_water = 0

while left < right:
    # 1. 갱신: 현재 포인터 위치의 벽 높이로 대장 벽 갱신
    left_max = max(left_max, blocks[left])
    right_max = max(right_max, blocks[right])

    # 2. 이동: 더 낮은 쪽 벽이 안쪽으로 이동 (높은 벽은 물 막아줘야 하니까 대기)
    if left_max <= right_max:
        total_water += left_max - blocks[left]
        left += 1
    else:
        total_water += right_max - blocks[right]
        right -= 1

print(total_water)