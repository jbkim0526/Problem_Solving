def solution(N, number):
    answer = -1

    dp = [0,set([N])]
    numbers = [0]
    num = 0
    for i in range(8):
        num = 10*num + N
        numbers.append(num)

    for i in range(2,9):
        s = set()
        s.add(numbers[i])
        l = []
        for j in range(1,i//2+1):
            for num1 in dp[j]:
                for num2 in dp[i-j]:
                    s.add(num1+num2)
                    s.add(num1-num2)
                    s.add(num2-num1)
                    s.add(num1*num2)
                    if num2 != 0 : s.add(int(num1/num2))
                    if num1 != 0 : s.add(int(num2/num1))
        dp.append(s)

    for i in range(1,9):
        if number in dp[i]:
            answer = i
            break

    return answer

print(solution(5, 12))