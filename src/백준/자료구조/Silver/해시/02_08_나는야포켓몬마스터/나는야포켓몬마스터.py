import sys
from collections import defaultdict
input=sys.stdin.readline

n,m=map(int,input().split())

# 1. defaultdict 선언 (기본값 타입 지정)
# - name_to_id: 키가 없으면 0을 리턴 (int() -> 0)
# - id_to_name: 키가 없으면 빈 문자열 리턴 (str() -> "")
# name_to_id = defaultdict(int)
# id_to_name = defaultdict(str)

name_to_id={}
id_to_name={}

for i in range(1,n+1):
    s=input().strip()
    name_to_id[s]=i
    id_to_name[i]=s

for i in range(m):
    s=input().strip()
    if s.isdigit():
        print(id_to_name[int(s)])
    else:
        print(name_to_id[s])



