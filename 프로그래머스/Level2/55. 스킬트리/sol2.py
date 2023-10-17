def solution(skill, skill_trees):
    answer = 0
    skill_list = list(skill)
    
    for st in skill_trees:
        s = ""
        for sk in st:
            if sk in skill_list:
                s += sk
        for i in range(len(s)):
            if s[i] != skill[i]:
                break
        else: answer += 1

    return answer



print(solution("CBD"	,["BACDE", "CBADF", "AECB", "BDA"]))