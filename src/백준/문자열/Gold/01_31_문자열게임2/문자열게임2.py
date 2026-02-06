import sys
from collections import defaultdict
input = sys.stdin.readline

def game():
    W = input().strip()
    try:
        K = int(input())
    except ValueError: # 혹시 모를 빈 줄 입력 방지용 (안전장치)
        return

    # K가 1일 때 예외처리 (선택사항이지만 넣으면 좋음)
    if K == 1:
        print(1, 1)
        return

    min_value = 1e9
    max_value = -1e9
    alp_dic = defaultdict(list)

    for index, word in enumerate(W):
        alp_dic[word].append(index)

    for key in alp_dic:
        indices = alp_dic[key]
        ind_len = len(indices)

        if ind_len < K:
            continue

        for i in range(ind_len - K + 1):
            start = indices[i]
            end = indices[i + K - 1]
            length = end - start + 1

            max_value = max(max_value, length)
            min_value = min(min_value, length)

    if min_value == 1e9:
        print(-1)
    else:
        print(min_value, max_value)

# T 입력 처리
line = input().strip()
if line:
    T = int(line)
    for _ in range(T):
        game()


# import sys
# from collections import defaultdict
#
# input = sys.stdin.readline
#
# def solve():
#     W = input().strip()
#     K = int(input())
#
#     # 1. 예외 처리: K가 1이면?
#     # 어떤 문자든 1개만 있으면 됨 -> 최소 길이 1, 최대 길이 1
#     if K == 1:
#         print("1 1")
#         return
#
#     # 2. 알파벳 별 인덱스 저장 (O(N))
#     char_indices = defaultdict(list)
#     for idx, char in enumerate(W):
#         char_indices[char].append(idx)
#
#     min_len = float('inf')
#     max_len = -1
#
#     # 3. 각 알파벳 별로 K개 간격 확인 (O(N))
#     for char in char_indices:
#         indices = char_indices[char]
#
#         # 해당 알파벳이 K개보다 적으면 볼 필요 없음
#         if len(indices) < K:
#             continue
#
#         # 슬라이딩 윈도우처럼 인덱스 계산
#         for i in range(len(indices) - K + 1):
#             # K개를 포함하는 구간의 시작점과 끝점
#             start_idx = indices[i]
#             end_idx = indices[i + K - 1]
#
#             # 길이 계산 (끝 - 시작 + 1)
#             length = end_idx - start_idx + 1
#
#             min_len = min(min_len, length)
#             max_len = max(max_len, length)
#
#     if min_len == float('inf'):
#         print(-1)
#     else:
#         print(min_len, max_len)
#
# T = int(input())
# for _ in range(T):
#     solve()