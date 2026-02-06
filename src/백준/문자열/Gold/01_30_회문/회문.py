import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    left = 0
    right = len(s) - 1
    ans = 0

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            check_left_deleted = s[left+1 : right+1]
            check_right_deleted = s[left : right]

            if check_left_deleted == check_left_deleted[::-1] or check_right_deleted == check_right_deleted[::-1]:
                ans = 1
            else:
                ans = 2
            break
    print(ans)



# import sys
# input = sys.stdin.readline
#
# # 2. 특정 구간이 회문인지 확인하는 보조 함수 (삭제 기회 없음)
# # 이 함수는 "이미 한 번 삭제한 후"에 호출되므로, 또 틀리면 바로 False입니다.
# def check_remainder(s, left, right):
#     while left < right:
#         if s[left] == s[right]:
#             left += 1
#             right -= 1
#         else:
#             return False # 기회를 이미 썼는데 또 틀림 -> 회문 불가
#     return True
#
# # 1. 메인 판별 함수
# def solve(s):
#     left, right = 0, len(s) - 1
#
#     while left < right:
#         # 문자가 같으면 계속 안쪽으로 진입
#         if s[left] == s[right]:
#             left += 1
#             right -= 1
#         else:
#             # ★ 문자가 다를 때! (여기가 핵심)
#             # 기회 1: 왼쪽 문자(left)를 지워본다 -> (left+1, right) 구간 검사
#             check1 = check_remainder(s, left + 1, right)
#
#             # 기회 2: 오른쪽 문자(right)를 지워본다 -> (left, right-1) 구간 검사
#             check2 = check_remainder(s, left, right - 1)
#
#             # 둘 중 하나라도 회문이 된다면 -> 유사회문(1)
#             if check1 or check2:
#                 return 1
#             # 둘 다 안 된다면 -> 일반 문자열(2)
#             else:
#                 return 2
#
#     # 반복문이 끝날 때까지 한 번도 안 틀렸다면 -> 진짜 회문(0)
#     return 0
#
# # 실행 코드
# T = int(input())
# for _ in range(T):
#     string = input().strip()
#     print(solve(string))