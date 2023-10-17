def solution(s):
    answer = True
    d = []

    for c in s:
        if c == ")": 
            if len(d) == 0:
                answer = False
                break 
            else:
                r = d.pop()
                if r != "(":
                    answer = False 
                    break  
        else: d.append(c)
    if len(d) != 0:
        answer = False
    return answer