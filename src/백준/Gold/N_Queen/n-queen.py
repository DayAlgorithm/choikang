import sys

n=int(sys.stdin.readline())

map=[0]*n
answer=0

# 가지치기
def check(row_index):
    for i in range(row_index):
        if map[row_index]==map[i] or abs(map[row_index]-map[i])==abs(row_index-i):
            return False
    return True

def dfs(row_index):
    global answer
    if row_index==n:
        answer+=1
        return

    for col_index in range(n):
        map[row_index]=col_index
        if check(row_index):
            dfs(row_index+1)

dfs(0)
print(answer)