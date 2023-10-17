def isValid(want, target,m):
    res = True
    for i in range(m):
        if want[i] > target[i]:
            res = False
            break
    return res
def solution(want, number, discount):
    answer = 0
    n = len(discount)
    m = len(want)
    l = [0]*m

    for i in range(10):
        if discount[i] in want:
            l[want.index(discount[i])] += 1
    if isValid(number,l,m):
        answer += 1
    for i in range(10,n):
        if discount[i-10] in want:
            l[want.index(discount[i-10])] -= 1
        if discount[i] in want:
            l[want.index(discount[i])] += 1
        if isValid(number,l,m):
            answer +=1 
    return answer






print(solution(["banana", "apple", "rice", "pork", "pot"]	,[3, 2, 2, 2, 1],	["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))