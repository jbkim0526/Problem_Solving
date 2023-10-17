# gridy 이긴한데, 변화된 수치를 재정렬하지 못함

def solution(n, lighthouse):
    answer = 0
    d_sort = [[i] for i in range(n+1)]
    d = [[] for i in range(n+1)]
    for light in lighthouse:
        a,b = light[0], light[1]
        d[a].append(b) ; d[b].append(a)
        d_sort[a].append(b) ; d_sort[b].append(a)
        

    d_sort.sort(key = lambda x: len(x))
    while n-1 > 0:
        l = d_sort.pop()
        i = l[0] ; nl = len(l)
        d[i] = []
        for j in range(1,nl):
            if i in d[l[j]]:
                d[l[j]].remove(i)
                n -= 1
        answer += 1

    return answer

print(solution(10,[[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]))