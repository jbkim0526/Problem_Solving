inf = 9
min_depth = inf

def solution(n, weaks, dists):
    dists.sort()
    def track(n,weaks,dists,depth):
        global min_depth
        if depth >= min_depth:
            return inf
        if len(weaks) == 0:
            min_depth = min(min_depth,depth)
            return depth
        if len(dists) == 0:
            return inf 
        dist = dists.pop()
        answers = []
        ranges = set()

        for weak in weaks:
            ranges.add(((weak - dist) % n ,weak))
            ranges.add((weak,(weak + dist) % n))

        for a,b in ranges:
            l = []
            if a > b : 
                for num in weaks:
                    if num >= a or num <= b:
                        continue 
                    l.append(num)
            else:
                for num in weaks:
                    if a <= num <= b:
                        continue 
                    l.append(num)

            answers.append(track(n,tuple(l),dists,depth+1))
            
        dists.append(dist)
        return min(answers)
    
    answer = track(n,tuple(weaks),dists,0)
    return answer if answer < inf else -1



print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))