min_count = 100

def f(l,count):
    global min_count
    if len(l) == 0:
        if min_count > count:
            min_count = count 
        return 
    temp = l.copy()
    n = temp.pop(0)
    if len(temp) == 0:
        if n >= 6:
            if min_count > count + (11-n):
                min_count = count + 11-n
        else:
            if min_count > count + n:
                min_count = count + n     
    else:
        if n == 0:
            f(temp,count)
        elif n == 10:
            temp[0] += 1
            f(temp,count)
        else:
            f(temp,count+n)
            temp2 = temp.copy()
            temp2[0] += 1
            f(temp2,count+(10-n))


def solution(storey):
    answer = 0
    l = []
    num = storey 
    while num > 0:
        l.append(num % 10)
        num = num // 10
    f(l,0)
    answer = min_count
    return answer



print(solution(9000))