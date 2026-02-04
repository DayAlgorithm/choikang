import sys

input=sys.stdin.readline()
n=int(input)
nums=list(map(int,sys.stdin.readline().split()))
op=list(map(int,sys.stdin.readline().split()))
selected_op=[]
min_value=1e9
max_value=-1e9

def dfs(depth):
    global min_value,max_value
    # 기저조건: 연산자의 개수가 수열의 개수-1이 될 때
    if depth==n-1:
        #첫번째 값 정해주기
        total=nums[0]
        # 연산자 개수만큼 반복하면서 기저조건의 세계관의 총합 구해주기가 안됨
        # 생각해보니까 nums 기준으로 안해줘도 되네
        for i in range(len(selected_op)): #0,1,2
            # 기호가 플러스라면
            if selected_op[i]==0:
                total+=nums[i+1]
            elif selected_op[i]==1:
                total-=nums[i+1]
            elif selected_op[i]==2:
                total*=nums[i+1]
            elif selected_op[i]==3:
                total=int(total/nums[i+1])
        min_value=min(min_value,total)
        max_value=max(max_value,total)
        return

    #연산자 개수 4만큼 반복
    for i in range(4):
        # 각 연산자가 0개가 되지 않을때까지
        if not op[i]==0:
            op[i]-=1
            selected_op.append(i)
            dfs(depth+1)
            selected_op.pop()
            op[i]+=1
dfs(0)
print(max_value)
print(min_value)