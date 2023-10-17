def solution(k, tangerine):
    answer = 0
    n = len(tangerine)
    l = {} 
    s = []

    for elem in tangerine:
        if elem in l:
            l[elem] += 1
        else: 
            l[elem] = 1

    for value in l.values():
        s.append(value)
    s.sort(key = lambda x : -x)
    while k > 0:
        if len(s) == 0:
            break
        count = s.pop(0)
        k -= count 
        answer += 1 
    return answer
