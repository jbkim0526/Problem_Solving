from collections import defaultdict

def solution(gems):
    answer = []
    n = len(gems)
    gem_count = len(set(gems))
    l = r = 0

    cur_set = set()
    cur_dict = defaultdict(int)

    while r < n+1:
        if len(cur_set) < gem_count:
            if r == n:
                break
            cur_gem = gems[r]
            cur_set.add(cur_gem)
            cur_dict[cur_gem] += 1
            r += 1
        elif len(cur_set) == gem_count:
            cur_gem = gems[l]
            if l+1 == r or cur_dict[cur_gem] <= 1:
                answer.append([l+1,r])
                cur_set.remove(cur_gem)
            cur_dict[cur_gem] -= 1
            l += 1

    answer.sort(key = lambda x: x[1]-x[0])
    return answer[0]

#print(solution(	["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["A","B","B","B","C","D","D","D","D","D","D","D","B","C","A"]))
