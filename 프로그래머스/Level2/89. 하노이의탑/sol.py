

def solution(n):

    d12 = [[[1,2]]]
    d13 = [[[1,3]]]
    d23 = [[[2,3]]]

    for i in range(1,n):
        nd13 = d12[i-1] + d13[0] + d23[i-1]
        nd12 = d13[i-1] + d12[0] + [x[::-1] for x in d23[i-1][::-1]] 
        nd23 = [x[::-1] for x in d12[i-1][::-1]]  + d23[0] + d13[i-1]
        d12.append(nd12)
        d13.append(nd13)
        d23.append(nd23)

    return d13[-1]


print(solution(15))
