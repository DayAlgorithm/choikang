# a c i s t w
# 4개가 되었는데 모음이 없으면 출력하지 않고 함수 반환

import sys
input=sys.stdin.readline

l,c=map(int,input().split())
chars=list(input().split())
chars_sorted=sorted(chars)
moum=["a","e","i","o","u"]
result=[]

# 함수
def dfs(depth,count):
# 기저조건 l과 result의 개수가 같다면
    if count==l:
        #모음
        mo=0
        #자음
        ja=0
        # 모음이 하나 이상에 자음은 최소 2개여야 한다
        for value in result:
            if value in moum:
                mo+=1
            else:
                ja+=1
        if mo>=1 and ja>=2:
            print("".join(result))
            return
        # 그외
        else:
            return

    for d in range(depth,c):
        result.append(chars_sorted[d])
        dfs(d+1,count+1)
        result.pop()

dfs(0,0)
