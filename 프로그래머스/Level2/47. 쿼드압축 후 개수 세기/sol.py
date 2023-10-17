def solution(arr):
    n = len(arr)
    n_zeros = 0
    n_ones = 0

    while n > 0:
        n = n//2
        for row in range(n):
            for col in range(n):
                r,c = 2*row, 2*col
                a1 = arr[r][c]
                a2 = arr[r][c+1]
                a3 = arr[r+1][c]
                a4 = arr[r+1][c+1]
                if a1 == a2 == a3 == a4 :
                    arr[row][col] = a1
                else:
                    arr[row][col] = -1
                    t = (a1,a2,a3,a4)
                    n_zeros += t.count(0)
                    n_ones += t.count(1)

    if arr[0][0] == 0 : n_zeros += 1 
    elif arr[0][0] == 1 : n_ones += 1

    return [n_zeros,n_ones]

print(solution([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))