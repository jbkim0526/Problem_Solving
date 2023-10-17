def solution(n, words):
    answer = [0,0]
    l = [words[0]]
    for i in range(1,len(words)):
        word = words[i]
        if word in l or word[0] != words[i-1][-1]:
            answer[0] = (i%n + 1)
            answer[1] = (i//n + 1)
            break
        l.append(word)
    return answer


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))