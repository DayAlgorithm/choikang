import sys
input=sys.stdin.readline

n=int(input())
calendar=[0]*367
for _ in range(n):
    s,e=map(int,input().split())
    #  1   2   3   4   5   6   7
    # [0] [1],[1],[2],[3],[0],[1]
    for i in range(s,e+1):
        calendar[i]+=1

w=0
h=0
total=0

for i in range(len(calendar)):
    if calendar[i]>0:
        w+=1
        h=max(h,calendar[i])
    else:
        total+=w*h
        w=0
        h=0

print(total)

























# import sys
# input = sys.stdin.readline
#
# def solve():
#     N = int(input())
#
#     # 1. 도화지 준비 (1일 ~ 365일, 여유분 포함 367칸)
#     # 마지막에 0을 만나야 계산이 끝나므로 넉넉하게 잡음
#     calendar = [0] * 367
#
#     # 2. 색칠하기 (Marking)
#     # 누가(Who) 칠하는지는 중요하지 않음. 몇 겹(How many)인지만 중요!
#     for _ in range(N):
#         s, e = map(int, input().split())
#         for i in range(s, e + 1):
#             calendar[i] += 1
#
#     # 3. 스캔하면서 면적 계산 (Scanning)
#     total_area = 0
#     w = 0       # 현재 덩어리의 가로 길이
#     h = 0       # 현재 덩어리의 최대 높이
#
#     for i in range(1, 367):
#         if calendar[i] > 0:
#             # [연속된 일정] 덩어리 확장 중
#             w += 1
#             h = max(h, calendar[i]) # 가장 높은 곳을 기준으로 직사각형 높이가 정해짐
#         else:
#             # [끊김] 빈 날짜(0)를 만남 -> 정산 타임!
#             if w > 0:
#                 total_area += w * h
#                 # 변수 초기화 (다음 덩어리를 위해)
#                 w = 0
#                 h = 0
#
#     print(total_area)
#
# solve()