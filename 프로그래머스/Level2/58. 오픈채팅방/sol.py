def solution(record):
    answer = []
    
    d = {}

    for r in record:
        l =  r.split()
        if l[0] in ["Enter","Change"]:
            d[l[1]] = l[2]

    for r in record:
        l =  r.split()
        if l[0] == "Enter":
            answer.append(d[l[1]]+"님이 들어왔습니다.")
        elif l[0] == "Leave":
            answer.append(d[l[1]]+"님이 나갔습니다.")

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))