def solution(number, k):
    answer = ''
    i = count = 0
    n = len(number)
    while count < k :
        s = number[i:i+k]
        i += 1
    answer += number[i:]
    return answer


print(solution("8"*1000000,	500000))