a = [5,10,1,2,9,6,4,3,8,7]

def swap(a,i,j):
    a[i],a[j] = a[j],a[i]
    
def sort(a):
    N = len(a)

    # i번에 들어갈 것 찾기
    for i in range(N):
        cur_min,cur_min_index = a[i],i

        # i에서 N-1까지 조사하면서 최소값
        for j in range(i+1,N):
            if cur_min > a[j]:
                cur_min,cur_min_index = a[j], j

        swap(a,i,cur_min_index)

    return a 

print(sort(a))



