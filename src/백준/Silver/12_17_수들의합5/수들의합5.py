import sys

n=int(sys.stdin.readline())

sum=1
start=1
end=1
count=1

while end!=n:
    if sum>n:
        sum-=start
        start+=1
    elif sum<n:
        end+=1
        sum+=end
    else:
        count+=1
        end+=1
        sum+=end

print(count)