
row = []

def isValid(j):
    for i in range(j):
        if row[i] == row[j] or abs(row[i]-row[j]) == abs(i-j):
            return False 
    return True

def track(i,n):
    ans = 0
    if i >= n:
        return ans + 1
    else:
        if n % 2 ==0 and i == 0 :
            for j in range(n//2):
                row[i] = j
                if isValid(i):
                    ans += track(i+1,n)
            ans *= 2
        else: 
            for j in range(n):
                row[i] = j
                if isValid(i):
                    ans += track(i+1,n)
    return ans

def solution(n):
    global row
    row = [0]*n
    answer = track(0,n)
    return answer

print(solution(10))