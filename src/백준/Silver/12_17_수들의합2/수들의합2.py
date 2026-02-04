import sys

n,m = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))

start=0
end=1
count=0
sum=nums[start]

while True:
    if sum<m:
        if end == n:
            break
        sum+=nums[end]
        end+=1
    elif sum>m:
        sum-=nums[start]
        start+=1
    elif sum==m:
        count+=1
        sum-=nums[start]
        start+=1

print(count)