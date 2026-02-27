import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

answer = []
result = 0

# 1,2,3,4,5 보고 나서
# 1,2/1,3/1,4/1,5  2,3/2,4/2,5  3/4,3/5  4/5 이런식으로 정해진 개수 만큼 확인해주는 식
# target_length: 이번 턴에 내가 몇 개를 뽑을 것인가? (님이 쓰신 m 역할)
def dfs(depth, count, target_length):
    global result

    # 목표한 개수만큼 배낭에 다 담았다면?
    if count == target_length:
        if sum(answer) == s: # 다 더해서 S가 되는지 확인!
            result += 1
        return

    # 님이 쓰신 완벽한 조합(for문) 로직!
    for i in range(depth, n):
        answer.append(nums[i])
        dfs(i + 1, count + 1, target_length)
        answer.pop()

# ==========================================
# 💡 핵심: 1개 뽑는 경우부터 N개 다 뽑는 경우까지 for문으로 돌려버린다!
# ==========================================
for m in range(1, n + 1):
    dfs(0, 0, m)

print(result)