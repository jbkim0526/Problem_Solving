def checkPalindrome(s):
    i = 0
    j = len(s)-1 
    if len(s) == 1:
        return False
    while i < j:
        if s[i] == s[j]:
            i += 1 
            j -= 1 
        else:
            return False 
    return True

def solution(s):
    answer = 1
    n = len(s)
    found = False
    for i in range(n):
        if n-i <= answer:
            return answer
        for j in range(n,i,-1):
            if not checkPalindrome(s[i:j]):
                continue
            answer = max(answer,j-i)
            break
    return answer


print(solution(	"abcde"))


