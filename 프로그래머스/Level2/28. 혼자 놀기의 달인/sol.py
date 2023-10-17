
def solution(cards):
    answer = 0
    n = len(cards)
    answers = []

    for i in range(n):
        if cards[i] == -1:
            continue
        index = i
        count = 0
        while cards[index] != -1:
            count += 1
            c = cards[index]
            cards[index] = -1
            index = c - 1
        answers.append(count)

    if len(answers) < 2:
        answer = 0
    else:
        answers.sort()
        answer = answers[-1] * answers[-2]
    return answer








print(solution([8,6,3,7,2,5,1,4]))