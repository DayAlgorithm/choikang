import sys
from collections import deque
input=sys.stdin.readline

T=int(input())

for _ in range(T):
    p=input().strip()
    n=int(input())
    str_list=input().strip()

    if n==0:
        q=deque()
    else:
        q=deque(str_list[1:-1].split(","))

    reverse_flag=False
    error_flag=False

    for func in p:
        if func=="R":
            reverse_flag=not reverse_flag
        elif func=="D":
            if q:
                if reverse_flag:
                    q.pop()
                elif reverse_flag==False:
                    q.popleft()
            else:
                error_flag=True
                break

    if error_flag:
        print("error")
    else:
        if reverse_flag:
            q.reverse()
        print("[" + ",".join(q) + "]")








#import sys
# from collections import deque
#
# # 1. 입출력 가속
# input = sys.stdin.readline
#
# def solve():
#     # 테스트 케이스 개수
#     T = int(input())
#
#     for _ in range(T):
#         p = input().strip() # 명령어 (RDD...)
#         n = int(input())    # 배열 크기
#         arr_str = input().strip() # 배열 문자열 "[1,2,3,4]"
#
#         # 2. 파싱 최적화 (Think Ultra)
#         # N이 0이면 빈 큐 생성, 아니면 파싱
#         # 숫자로 변환(map(int, ...)) 하지 않고 문자열 그대로 저장! -> 속도 향상
#         if n == 0:
#             q = deque()
#         else:
#             # [1:-1]로 대괄호 제거 후 콤마로 분리
#             q = deque(arr_str[1:-1].split(','))
#
#         is_reversed = False # 뒤집힘 상태 플래그
#         is_error = False    # 에러 상태 플래그
#
#         # 3. 명령어 처리
#         for cmd in p:
#             if cmd == 'R':
#                 is_reversed = not is_reversed
#             elif cmd == 'D':
#                 if not q:
#                     is_error = True
#                     break
#
#                 # 뒤집혔으면 뒤(pop)에서, 아니면 앞(popleft)에서 제거
#                 if is_reversed:
#                     q.pop()
#                 else:
#                     q.popleft()
#
#         # 4. 결과 출력
#         if is_error:
#             print("error")
#         else:
#             # 최종 상태가 뒤집혀있으면, 이때 딱 한 번 진짜로 뒤집음
#             if is_reversed:
#                 q.reverse()
#
#             # 문자열 상태 그대로 join (매우 빠름)
#             print("[" + ",".join(q) + "]")
#
# if __name__ == "__main__":
#     solve()