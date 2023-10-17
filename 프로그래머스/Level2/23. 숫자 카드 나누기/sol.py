
def gcf(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def solution(arrayA, arrayB):
    answer = 0

    arrayA.sort()
    arrayB.sort()
    nA = len(arrayA)
    nB = len(arrayB)
    gcfA = arrayA[0]
    gcfB = arrayB[0]

    for i in range(1, nA):
        gcfA = gcf(arrayA[i],gcfA)

    for i in range(1, nB):
        gcfB = gcf(arrayB[i],gcfB)

    if gcfA == 1 and gcfB == 1:
        return answer 
    elif gcfA == 1 and gcfB != 1:
        for i in range(nA):
            if arrayA[i] % gcfB == 0:
                return answer 
        answer = gcfB 
    elif gcfA != 1 and gcfB == 1:
        for i in range(nB):
            if arrayB[i] % gcfA == 0:
                return answer 
        answer = gcfA 
    else:
        isA = True 
        isB = True
        for i in range(nA):
            if arrayA[i] % gcfB == 0:
                isB = False
                break 
        for i in range(nB):
            if arrayB[i] % gcfA == 0:
                isA = False 
                break 
        if isA and isB :
            answer = max(gcfA, gcfB)
        elif isA and not isB:
            answer = gcfA 
        elif not isA and isB:
            answer = gcfB 
    
    return answer

print(solution([14, 35, 119],	[18, 30, 102]))