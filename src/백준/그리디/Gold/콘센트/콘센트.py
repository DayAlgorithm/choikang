import sys
import heapq
input=sys.stdin.readline
#n:전자기기 m:콘센트
n,m=map(int,input().split())
# 1,4,4,8,1
times=list(map(int,input().split()))
# 8,4,4,1,1
times.sort(reverse=True)
rs=[]
# 전자기기의 개수가 콘센트보다 작거나 같다면
if len(times)<=m:
    print(max(times))
else:
    for i in range(m):
        heapq.heappush(rs,(times[i]))

    for i in range(m,n):
        min_time=heapq.heappop(rs)
        time=times[i]
        heapq.heappush(rs,(min_time+time))

    print(max(rs))

















# import sys
# import heapq
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# times = list(map(int, input().split()))
#
# # 1. 내림차순 정렬 (필수)
# times.sort(reverse=True)
#
# # [예외 처리 혹은 최적화]
# # 기기가 콘센트보다 적거나 같으면?
# # 그냥 제일 오래 걸리는 거 하나 꽂아두면 끝나는 시간임.
# if N <= M:
#     print(times[0]) # 정렬했으니 맨 앞이 최대
#     sys.exit()
#
# # 2. 초기화: 처음 M개를 힙에 넣는다! (0 안 넣음)
# # 콘센트 M개에 일단 기기 M개를 꽉 채워 꽂고 시작하는 겁니다.
# outlets = []
# for i in range(M):
#     heapq.heappush(outlets, times[i])
#
# # 3. 남은 기기들(M번째부터 끝까지) 처리
# for i in range(M, N):
#     # 가장 빨리 비는 콘센트(min)를 찾아서
#     min_val = heapq.heappop(outlets)
#     # 다음 기기를 이어서 꽂음 (시간 누적)
#     heapq.heappush(outlets, min_val + times[i])
#
# # 4. 정답
# print(max(outlets))