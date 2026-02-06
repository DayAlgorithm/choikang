import sys
from collections import Counter
from collections import defaultdict
input=sys.stdin.readline
n,m=map(int,input().split())

data = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']

cnt=Counter(data)
print(cnt)
print('apple')

d=defaultdict(int)

for i in data:
    d[i]+=1

print(d)
