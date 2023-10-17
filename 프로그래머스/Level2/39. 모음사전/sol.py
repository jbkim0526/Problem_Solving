alpha = ["A", "E", "I", "O", "U"]
end = False

def track(word, s):
    global end
    count = 1 
    if len(s) >= 5:
        return count
    for c in alpha:
        if s+c == word:
            end = True
            break
        else:
            if not end:
                count += track(word, s + c)
    return count


def solution(word):
    answer = track(word,"")
    return answer

print(solution("I"))