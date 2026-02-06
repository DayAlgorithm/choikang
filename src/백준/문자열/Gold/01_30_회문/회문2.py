import sys
input=sys.stdin.readline

def is_palindrome(str):
    start=0
    end=len(str)-1
    while(start<end):
        if str[start]==str[end]:
            start+=1
            end-=1
        else:
            return False
    return True


def palindrome(str):
    start=0
    end=len(str)-1

    while(start<end):
        if str[start]==str[end]:
            start+=1
            end-=1
        else:
            left_str=str[start:end]
            right_str=str[start+1:end+1]
            if is_palindrome(left_str) or is_palindrome(right_str):
                print(1)
            else:
                print(2)
            return
    print(0)

T=int(input())
for _ in range(T):
    str=input().strip()
    palindrome(str)
