# ababaa
# aba, bab, aba, baa, aab
# abab, baba, abaa, baab, aaba
# abab,baba,abaa,baaa,aaab,aaba
# 길이가 n이면 몇개로 슬라이싱 하든 길이만큼은 무조건 슬리이싱 되는게 끝과 앞이 연결되어 있기 때문에
import sys

input=sys.stdin.readline
s=input().strip()
k=s.count("a")
l=len(s)
min_value=1e9
#6 0,1,2,3,4,5
for i in range(l):
    b_count=0
    #4 0,1,2,3
    for j in range(k):
       if s[(i+j)%l]=="b":
           b_count+=1
    min_value=min(min_value,b_count)

print(min_value)

































import sys
input = sys.stdin.readline

s = list(input().strip())
k = s.count("a")
n = len(s)  # 길이를 변수에 담아두면 편합니다

min_value = 1e9

# [수정 1] 원형이므로 시작점은 문자열 끝까지 가야 합니다.
# range(n - k + 1) -> range(n) 으로 변경
for i in range(n):

    b_count = 0

    # [수정 2] start, end 변수 대신, 단순히 k번 반복하게 변경
    # start부터 k개만큼 확인
    for j in range(i, i + k):
        # 만약 j가 길이(n)를 넘어가면?
        # 예: 길이가 10인데 인덱스가 12가 되면 -> 2번 인덱스를 봐야 함
        target_index = j % n

        if s[target_index] == "b":
            b_count += 1

    min_value = min(min_value, b_count)

print(min_value)


