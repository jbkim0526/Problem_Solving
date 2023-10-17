def solution(str1, str2):
    answer = 0
    n1, n2 = len(str1), len(str2)
    d1 = {} ; d2 = {}
    union = 0
    intersection = 0

    for i in range(n1-1):
        a, b = str1[i],str1[i+1]
        if a.isalpha() and b.isalpha():
            k = a.lower()+b.lower()
            if k in d1:
                d1[k] += 1
            else:
                d1[k] = 1
    
    for i in range(n2-1):
        a, b = str2[i],str2[i+1]
        if a.isalpha() and b.isalpha():
            k = a.lower()+b.lower()
            if k in d2:
                d2[k] += 1
            else:
                d2[k] = 1

    for key in d1.keys():
        if key in d2:
            union += max(d1[key],d2[key])
            intersection += min(d1[key],d2[key])
        else:
            union += d1[key]

    for key in d2.keys():
        if key not in d1:
            union += d2[key]

    if union == intersection == 0:
        answer = 65536
    else:
        answer = int(intersection/union*65536)
    return answer

print(solution("handshake",	"shake hands"))