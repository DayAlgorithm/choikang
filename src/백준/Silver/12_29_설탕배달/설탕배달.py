import sys

n=int(sys.stdin.readline())

inf = float('inf')
dp=[inf] * 5006

dp[3]=1
dp[5]=1

for i in range(6,n+1):
    dp[i] = min(dp[i-3],dp[i-5])+1

if(dp[n]==inf):
    print("-1")
else:
    print(dp[n])
