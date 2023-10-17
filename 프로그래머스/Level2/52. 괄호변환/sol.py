
def solution(p):
    answer = ""
    if not p: 
        return answer 
    else:
        left = right = 0
        count = 0
        isValid = True
        u = v = "" 
        
        for i in range(len(p)):
            if p[i] =="(": 
                count += 1
                left += 1
            else: 
                if count == 0:
                    isValid = False
                else:
                    count -= 1
                right += 1
            if left == right and left > 0:
                u, v = p[:i+1],p[i+1:]
                break
        if isValid:
            answer = u + solution(v)
        else:
            u = "".join(list(map(lambda x: "(" if  x == ")" else ")", u[1:-1])))
            answer = "("+ solution(v) +")"+ u
 
    return answer

print(solution("()))((()"))