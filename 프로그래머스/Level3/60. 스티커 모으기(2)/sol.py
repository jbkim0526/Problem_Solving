


def solution(sticker):
    answers = []
    n = len(sticker)

    def getMaxSum(i,sticker):
        answer = 0
        answer += sticker[i]
        sticker[i] = 0
        sticker[(i-1)%n] = 0
        sticker[(i+1)%n] = 0
        i = (i+2) % n
        while sticker[i]:
            if sticker[i]+sticker[(i+2)%n] > sticker[(i+1)%n]:
                answer += sticker[i]
                sticker[(i+1)%n] = 0
                sticker[i] = 0
                i = (i+2) % n 
            else:
                answer += sticker[(i+1)%n]
                sticker[(i+2)%n] = 0
                sticker[i] = 0
                sticker[(i+1)%n] = 0
                i = (i+3) % n 
        return answer

    for i in range(n):
        answers.append(getMaxSum(i,sticker.copy()))

    return max(answers)



print(solution([14, 6, 5, 11, 3, 9, 2, 10]))