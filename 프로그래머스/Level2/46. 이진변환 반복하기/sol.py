def solution(s):
    answer = []
    rem_zeros = 0
    count = 0
    while True:
        if s == "1":
            break
        n = len(s)
        n_one = s.count("1")
        rem_zeros += (n-n_one)  
        s = bin(n_one)[2:]
        count += 1
    answer.append(count)
    answer.append(rem_zeros)

    return answer

print(solution("110010101001"))