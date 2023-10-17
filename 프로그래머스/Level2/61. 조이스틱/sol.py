
def track(l,total,n,index):
    if total >= n:
        return 0
    candidates = []
    for i in range(1,n):
        ni = (index +i) % n 
        if not l[ni]:
            candidates.append((ni,min(i,n-i)))
            break 
    for i in range(1,n):
        ni = (index - i) % n 
        if not l[ni]:
            candidates.append((ni,min(i,n-i)))
            break 
    ans = 20
    for i,diff in candidates:
        temp = l.copy() ; temp[i] = 1
        ans = min(ans,track(temp,total+1,n,i)+diff)
    return ans

def solution(name):
    answer = 0
    n = len(name)
    l = [1]+[0]*(n-1)
    AA , AZ = ord("A"), ord("Z")
    for i in range(n):
        c = name[i]
        if c == "A": 
            l[i] = 1
        else:
            AC = ord(c)
            answer += min(abs(AC-AA), abs(AZ-AC+1))
    answer += track(l,sum(l),n,0)

    return answer

print(solution("BBBBAAAABA"))