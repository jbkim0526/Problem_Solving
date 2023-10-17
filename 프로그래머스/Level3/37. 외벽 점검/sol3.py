def solution(n, weaks, dists):
    inf = 9
    dists.sort()
    dp = [dict() for _ in range(len(dists))]

    def track(n,weaks,dists,depth):
        if len(weaks) == 0:
            return depth
        if len(dists) == 0:
            return inf 
        if weaks in dp[depth]:
            return dp[depth][weaks]

        dist = dists.pop()
        answers = []
        ranges = set()

        for weak in weaks:
            ranges.add(((weak-dist)%n ,weak))
            ranges.add((weak,(weak+dist)%n))

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
        ans = min(answers)
        dp[depth][weaks] = ans
        return ans
    
    answer = track(n,tuple(weaks),dists,0)
    return answer if answer < inf else -1



print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))