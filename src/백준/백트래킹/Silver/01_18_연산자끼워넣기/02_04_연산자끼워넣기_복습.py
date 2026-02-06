import sys
input=sys.stdin.readline

n=int(input())
s=list(map(int,input().split()))
op=list(map(int,input().split()))
max_value=-1e9
min_value=1e9
selected_ops=[]

def dfs(count):
    global max_value,min_value
    if n-1==count:
        # s_sum=처음값
        s_sum=s[0]
        # s=[3,2,1]
        for i in range(len(s)-1):
            if selected_ops[i]==0:
                s_sum+=s[i+1]
            elif selected_ops[i]==1:
                s_sum-=s[i+1]
            elif selected_ops[i]==2:
                s_sum*=s[i+1]
            else:
                s_sum=int(s_sum/s[i+1])
        max_value=max(max_value,s_sum)
        min_value=min(min_value,s_sum)
        return

    # n=5
    # op=[1,2,0,1]
    # index가 없어도 되는 이유가 원래는 필요한데 op리스트가 그 역할을 대신 해주고 있음
    for i in range(len(op)):
        # while 써서 2가 0이 될때까지 해주면 안됨 그러면 무조건 +연산자는 ++가 붙어있게 됨
        if op[i]!=0:
            op[i]-=1
            selected_ops.append(i)
            dfs(count+1)
            op[i]+=1
            selected_ops.pop()

dfs(0)
print(max_value)
print(min_value)