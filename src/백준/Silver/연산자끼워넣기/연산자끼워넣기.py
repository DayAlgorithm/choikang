import sys
n=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split())) # 2,3
op_counts=list(map(int,sys.stdin.readline().split())) # 1112
min_value=1e9
max_value=-1e9
selected_op=[]

def dfs(depth):
    global min_value,max_value
    #깊이가 n과 같아지면 즉 숫자가 목표하는 n만큼 전부 선택되면
    if depth==n-1:
        # 더해지기 전해 처음 값은 고정
        now=nums[0]
        # 숫자가4개면 연산자는3개 n-1만큼 반복
        for i in range(n-1):
            # now의 값을 점차 연산해주는데 +,-각 연산자의 경우일떄를 나눠줌
            if selected_op[i]==0:
                now+=nums[i+1]
            elif selected_op[i]==1:
                now-=nums[i+1]
            elif selected_op[i]==2:
                now*=nums[i+1]
            elif selected_op[i]==3:
                now=int(now/nums[i+1])

        min_value=min(min_value,now)
        max_value=max(max_value,now)
        return

    #연산자를 선택
    for i in range(4):
        if op_counts[i]>0:
            op_counts[i]-=1
            selected_op.append(i)
            dfs(depth+1)
            selected_op.pop()
            op_counts[i]+=1

dfs(0)
print(max_value)
print(min_value)


