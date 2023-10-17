def solution(msg):
    answer = []
    d = {}
    for i in range(65,91):
        d[chr(i)] = i-64
    i = 0 ; num = 27 ; msg_len = len(msg)
    while i < msg_len:
        j = i+1 ; w = None ; wi = -1
        while j < msg_len+1:
            m = msg[i:j]
            if m in d: w = m ; wi = j
            j += 1
        answer.append(d[w])
        wpc = msg[i:wi+1]
        if wpc not in d:
            d[wpc] = num 
            num += 1
        i = wi
    return answer

print(solution("TOBEORNOTTOBEORTOBEORNOT"))