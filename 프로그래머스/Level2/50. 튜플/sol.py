def solution(s):
    answer = []
    index = 1
    l = []
    for i in range(1,len(s)):
        if s[i] == "}":
            l.append(s[index+1:i].split(","))
            index = i+2
    l.pop()
    l.sort(key = lambda x: len(x))
    for elem in l:
        for i in elem:
            num = int(i)
            if num not in answer:
                answer.append(num)
                break

    return answer