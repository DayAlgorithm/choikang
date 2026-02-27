# 3
# 9
# 2 1 4 3 5 6 2 7 2
import sys
input=sys.stdin.readline

n=int(input())
total_rec=int(input())
rec=list(map(int,input().split()))

frames={}

for i,value in enumerate(rec):
    if value in frames:
        frames[value][0]+=1
    else:
        if len(frames)==n:
            target=min(frames, key=lambda x: (frames[x][0], frames[x][1]))
            del frames[target]
        frames[value]=[1,i]

ans=sorted(frames.keys())
print(*ans)

# import sys
# input = sys.stdin.readline
#
# # 1. 입력 받기
# N = int(input())
# total_recs = int(input())
# recs = list(map(int, input().split()))
#
# # 2. 사진틀을 딕셔너리로 선언!
# # 형태: { 학생번호: [추천수, 들어온시간] }
# frames = {}
#
# # 3. 시뮬레이션 시작
# for time, student in enumerate(recs):
#
#     # [CASE 1] 이미 사진틀에 있는 학생이라면? (미친 속도 O(1))
#     if student in frames:
#         frames[student][0] += 1  # 추천수만 1 증가
#
#     # [CASE 2] 사진틀에 없는 새로운 학생이라면?
#     else:
#         # 자리가 꽉 찼는지 확인
#         if len(frames) >= N:
#             # [치트키 발동] 딕셔너리에서 쫓아낼 놈 찾기
#             # frames.keys() 중에서 (추천수, 들어온시간)이 가장 작은 키(학생번호)를 찾음
#             target = min(frames, key=lambda k: (frames[k][0], frames[k][1]))
#
#             # 찾은 타겟을 딕셔너리에서 삭제!
#             del frames[target]
#
#         # 빈자리에 새로운 학생 추가
#         frames[student] = [1, time]
#
# # 4. 최종 출력 (딕셔너리의 키값(학생번호)만 뽑아서 오름차순 정렬)
# ans = sorted(frames.keys())
# print(*ans)

