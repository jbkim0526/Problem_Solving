

def solution(s):
    n = len(s)
    answer = n 
    for unit in range(1,n//2+1):
        unit_string = s[0:unit]
        count,cont,isCont = 0,0,False
        for i in range(unit, n+1-unit, unit):
            target = s[i:i+unit]
            
            if target == unit_string:
                if isCont : count += unit ; cont += 1
                else: count += unit-1 ; isCont = True ; cont += 2
                if cont == 10 : count -= 1
                elif cont == 100: count -= 1
                elif cont == 1000: count -= 1
            else:
                if isCont : cont = 0
                unit_string = target ; isCont = False
        answer = min(answer, n-count)
    return answer


print(solution("a"*1000))