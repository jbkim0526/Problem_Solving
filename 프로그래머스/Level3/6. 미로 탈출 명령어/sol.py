from heapq import heapify, heappop, heappush

def solution(n, m, x, y, r, c, k):
    answer = ''
    check = (k-abs(x-r)-abs(y-c))
    if check < 0 or check % 2 != 0:
        answer = "impossible"
    else:
        directions = [(1,0),(0,-1),(0,1),(-1,0)]
        dir_names = ["d","l","r","u"]
        reverse = ["u","r","l","d"]
        ipath = "d"*(r-x) if r-x > 0 else "u"*(x-r)
        jpath = "r"*(c-y) if c-y > 0 else "l"*(y-c)
        heap = list(ipath+jpath)
        i = x ; j = y
        while k > len(heap):
            for index,(di,dj) in enumerate(directions):
                if 1<=i+di<=n and 1<=j+dj<=m:
                    dir_name = dir_names[index]
                    answer += dir_names[index]
                    if dir_name in heap:
                        heap.remove(dir_name)
                    else:
                        heap.append(reverse[index])  
                    i += di ; j += dj
                    break
            k -= 1
        heapify(heap)
        while len(heap)>0:
            answer += heappop(heap)
    return answer

print(solution(3,4,2,3,3,1,5))