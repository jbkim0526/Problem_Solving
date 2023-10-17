def solution2(n, l, r):
    answer = 0

    for l in range(l-1, r):
        if check(l):
            answer += 1

    return answer

def check(i):
    if i % 5 == 2:
        return False
    if i < 5:
        return True


    return check(i // 5)



def solution(n, l, r):
    answer = 0
    unit = [1,1,0,1,1]
    l_list = []
    r_list = []
    curr_l = l-1
    curr_r = r-1
    isGroup = False
    lisZero = False 
    risZero = False
    for i in range(n):
        l_list.append(curr_l % 5)
        r_list.append(curr_r % 5)
        curr_l //= 5 
        curr_r //= 5

    if n == 1:
        answer += sum(unit[l_list[0]:r_list[0]+1])
        return answer 
    else:
        for i in reversed(range(n)):
            i_l = l_list[i]
            i_r = r_list[i]
            print(i_l, i_r)
            if i == n-1:
                if i_l == 2:
                    lisZero = True 
                if i_r == 2:
                    risZero = True

                if i_l == i_r:
                    if lisZero:
                        break
                    isGroup = True
                else:
                    answer += sum(unit[i_l+1:i_r])*(4**i)
                    isGroup = False
            elif i == 0:
                lsum = 0
                rsum = 0
                if isGroup:
                    answer += (sum(unit[i_l:i_r+1]))*(4**i)
                else:
                    if not lisZero:
                        lsum = sum(unit[i_l:])
                    if not risZero:
                        rsum = sum(unit[:i_r+1])
                    answer += (lsum+rsum)*(4**i)
            else:
                if isGroup :
                    if i_l != i_r :
                        if i_l == 2:
                            lisZero = True 
                        if i_r == 2:
                            risZero = True
                        answer += (sum(unit[i_l+1:i_r]))*(4**i)
                        isGroup = False
                    else:
                        if i_l == 2:
                            break
                else:
                    lsum = 0
                    rsum = 0
                    if not lisZero:
                        lsum = sum(unit[i_l+1:])
                    if not risZero:
                        rsum = sum(unit[:i_r])
                    if i_l == 2:
                        lisZero = True 
                    if i_r == 2:
                        risZero = True
                    answer += (lsum+rsum)*(4**i)
    return answer

#print(solution(4,27,68))


n = 0
for i in range(1,5**n):
    for j in range(i,5**n):
        if solution(n,i,j) != solution2(n, i, j):
            print(n,i,j)
            break

print(solution(3, 1, 36))
#print(solution2(3,1,36))
