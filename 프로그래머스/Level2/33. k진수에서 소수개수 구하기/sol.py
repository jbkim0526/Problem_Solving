
def isPrime(n):
    if n == 1:
        return False

    ans = True
    m = int(n**(1/2))
    for i in range(2,m+1):
        if n % i == 0:
            ans = False
            break
    return ans

def solution(n, k):
    answer = 0

    k_num = ''
    while n > 0 :
        k_num = str(n % k)+ k_num
        n //= k
    l = k_num.split('0')
    for elem in l:
        if elem == '':
            continue 
        else: 
            if isPrime(int(elem)):
                answer += 1
    return answer

print(solution(110011, 10))
