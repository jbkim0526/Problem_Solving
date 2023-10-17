from collections import deque
def solution(n, weaks, dists):
    dists.sort()
    inf = 9
    answer = inf
    weaks_set = set(weaks)
    def track(n,weaks,dists,depth):
        nonlocal answer
        if depth >= answer:
            return inf
        if len(weaks) == 0:
            answer = min(answer,depth)
            return depth
        if len(dists) == 0:
            return inf 
        dist = dists.pop()
        answers = []
        ranges = set()

        cur_deque = deque()
        new_weak_set = set()
        print(dist)
        for i in range(n-dist+1):
            if i in weaks_set:
                cur_deque.append(i)
        print(cur_deque)
        new_weak_set.add(tuple(cur_deque))
        for i in range(1,n):
            if i == cur_deque[0]:
                cur_deque.popleft()
            v = (n-dist+i)%n
            if v in weaks_set:
                cur_deque.append(v)
                new_weak_set.add(tuple(cur_deque))

        print(new_weak_set)
        # for weak in weaks:
        #     a = (weak - dist) % n 
        #     b = (weak + dist) % n
        #     ranges.add((a,weak))
        #     ranges.add((weak,b))

        # new_weak_set = set()

        # for a,b in ranges:
        #     l = []
        #     if a > b : 
        #         for num in weaks:
        #             if num >= a or num <= b:
        #                 continue 
        #             l.append(num)
        #     else:
        #         for num in weaks:
        #             if a <= num <= b:
        #                 continue 
        #             l.append(num)
        #     new_weak_set.add(tuple(l))

        for new_weaks in new_weak_set:
            answers.append(track(n, new_weaks,dists,depth+1))
        dists.append(dist)
        return min(answers)
    
    track(n,weaks,dists,0)
    return answer


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))