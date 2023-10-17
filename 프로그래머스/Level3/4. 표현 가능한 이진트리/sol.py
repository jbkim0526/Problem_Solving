def isValid(s, isZero):
    if len(s) == 1:
        if not isZero:
            return True
        else:
            return s != "1"
    n = len(s)//2 ; mid = s[n]
    if isZero and mid == "1":
        return False
    if mid == "0":
        return isValid(s[:n],True) and isValid(s[n+1:],True)
    else:
        return isValid(s[:n],isZero) and isValid(s[n+1:],isZero)
        
def solution(numbers):
    answer = []
    tree_sizes = [1,3,7,15,31,63]
    for num in numbers:
        s = ""; temp = bin(num);  n = len(temp)-2
        for tree_size in tree_sizes:
            if tree_size >= n:
                s = "0"*(tree_size-n)+temp[2:]
                break 
        if isValid(s,False):
            answer.append(1)
        else:
            answer.append(0)
    return answer

print(solution([int("1110010",2)]))