from collections import defaultdict

def isValid(user,ban):
    if len(user) != len(ban):
        return False
    for i in range(len(ban)):
        if ban[i] == "*":
            continue 
        if user[i] != ban[i]:
            return False 
    return True

def solution(user_ids, banned_ids):
    answer = []
    banned_len = len(banned_ids) 
    banned_id_set = set(banned_ids)
    banned_candidates =  defaultdict(list)

    for banned_id in banned_id_set:
        for user_id in user_ids:
            if isValid(user_id,banned_id):
                banned_candidates[banned_id].append(user_id)

    def track(case, depths):
        if depths >= banned_len:
            answer.append(case)
            return
        for user_id in banned_candidates[banned_ids[depths]]:
            if user_id in case:
                continue 
            new_case = case.copy()
            new_case.add(user_id)
            track(new_case,depths+1)
        return

    track(set(),0)
    answer_set = set()
    for s in answer:
        l = list(s)
        l.sort()
        answer_set.add(tuple(l))

    return len(answer_set)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))