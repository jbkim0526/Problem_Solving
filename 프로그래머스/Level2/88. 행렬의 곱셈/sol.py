def solution(arr1, arr2):
    answer = []
    m, r, n = len(arr1), len(arr1[0]),len(arr2[0])

    for row in arr1:
        temp = []
        for j in range(n):
            s = 0
            for i in range(r):
                s += row[i]*arr2[i][j]
            temp.append(s)
        answer.append(temp)
    return answer

print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],[[5, 4, 3], [2, 4, 1], [3, 1, 1]]))