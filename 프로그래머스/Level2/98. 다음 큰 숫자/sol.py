def solution(n):
    s = bin(n)[2:]
    res =""
    m = len(s)
    fi = -1 ; li = 0 ; i = m-1
    while i >= 0:
        if s[i] == "1":
            if fi == -1: fi = i
        else:
            if fi != -1:
                li = i+1
                break
        i -= 1
    if fi == li:
        if li == 0:
            res = "10"+s[fi+1:]
        else:
            res = s[:li-1] +"10"+ s[fi+1:]
    else:
        count = fi-li
        if li == 0:
            res = "1"+"0"*(m-li-count)+"1"*(count)
        else:
            res = s[:li-1]+"1"+"0"*(m-li-count)+"1"*(count)
    return int(res,2)

print(solution(78))