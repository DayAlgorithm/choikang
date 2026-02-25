import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

answer = []
count=0

def dfs(depth):
    global count

    if len(answer)>0 and sum(answer)==s:
        count+=1

    for i in range(depth,n):
        answer.append(nums[i])
        dfs(i+1)
        answer.pop()

dfs(0)
print(count)