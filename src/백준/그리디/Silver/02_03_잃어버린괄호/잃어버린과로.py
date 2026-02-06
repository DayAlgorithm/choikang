import sys
input=sys.stdin.readline
#10+20+30-30+40-30
s=input().strip()
#["10+20+30","30+40","30"]
s_minus=s.split("-")
rs=0

for index,value in enumerate(s_minus):
    s_plus=value.split("+")
    s_sum=0
    for p in s_plus:
        s_sum+=int(p)

    if index==0:
        rs+=s_sum
    else:
        rs-=s_sum

print(rs)































# import sys
# input = sys.stdin.readline
#
# # 1. 입력 문자열을 받아서 '-' 기준으로 쪼갭니다.
# # Java: String[] groups = expression.split("-");
# expression = input().strip()
# groups = expression.split('-')
#
# result = 0
#
# # 2. 배열의 인덱스를 이용해 반복문을 돕니다.
# # Java: for (int i = 0; i < groups.length; i++) { ... }
# for i in range(len(groups)):
#
#     # 3. 현재 덩어리 (예: "50+40") 가져오기
#     current_group = groups[i]
#
#     # 4. 이 덩어리의 합계를 구하기 위한 임시 변수
#     temp_sum = 0
#
#     # 5. '+' 기준으로 다시 쪼개서 숫자로 변환해 더합니다.
#     # Java: String[] tempParts = current_group.split("\\+");
#     # Java: for (String part : tempParts) { temp_sum += Integer.parseInt(part); }
#     temp_parts = current_group.split('+')
#     for part in temp_parts:
#         temp_sum += int(part)
#
#     # 6. ★ 핵심 로직 ★
#     # 맨 첫 번째 그룹(i == 0)만 '양수'이고,
#     # 나머지는 '-' 뒤에 있던 애들이니 모두 '뺄셈' 처리합니다.
#     if i == 0:
#         result += temp_sum
#     else:
#         result -= temp_sum
#
# print(result)