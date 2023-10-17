def getstr(n, number):
    s = ""
    d = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",
        9:"9",10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    if number == 0: return '0'
    while number > 0:
        s = d[number % n] + s
        number //= n 
    return s


def solution(n, t, m, p):
    answer = ""
    l = []
    num = 0
    while len(l) < m*t:
        for c in getstr(n,num):
            l.append(c)
        num += 1
    for i in range(t):
        answer += l[p-1+i*m]
    return answer

print(getstr(2, 3))
print(solution(2,4,2,1))
