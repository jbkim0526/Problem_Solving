def solution(s):
    answer = ""
    l = s.split(" ")
    for c in l:
        if not c :
            answer += " "
        else:
            if c[0].isalpha(): answer += c[0].capitalize()
            else: answer += c[0]
            answer+= c[1:].lower()+" "
    return answer[:-1]

print(solution("3people   unFollowed  me"))