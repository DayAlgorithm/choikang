import sys
input=sys.stdin.readline

h,w=map(int,input().split())
# [3 0 1 4]
blocks=list(map(int,input().split()))

count=0
left,right=0,(w-1)

left_max=blocks[left]
right_max=blocks[right]

while left<right:
    # 1. 갱신: 현재 포인터 위치의 벽 높이로 대장 벽 갱신
    left_max=max(left_max,blocks[left])
    right_max=max(right_max,blocks[right])
    # 2. 이동: 더 낮은 쪽 벽이 안쪽으로 이동 (높은 벽은 물 막아줘야 하니까 대기)
    if left_max<right_max:
        count+=left_max-blocks[left]
        left+=1
    # 최대 블록갯수는 내가 될수도 있고 내 왼쪽이 될 수도 있어 그러면 왼쪽 오른쪽 비교하기 전에
    # 현재 내블록과 이전 최대 왼쪽블록을 비교하고 최대를 정했으면 그거랑 현재만 비교하면 돼 왼쪽 포인터의 위치가 포인트가 아님
    else:
        count+=right_max-blocks[right]
        right-=1

print(count)
