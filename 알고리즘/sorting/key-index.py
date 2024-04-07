value = ["Anderson","Brown","Davis","Garcia","Harris","Jackson","Martin","Robinson"]
key = [2,3,3,4,1,3,1,2]


def sort(value, key):
    # R: distinct한 key의 개수
    N,R = len(key), 4
    counts = [0]*(R+1)
    aux = [None]*(N)

    # get count
    for i in range(N):
        counts[key[i]] += 1

    for i in range(1,R+1):
        counts[i] += counts[i-1]

    for i in range(N):
        aux[counts[key[i]-1]] = value[i]
        counts[key[i]-1] += 1

    print(aux)


sort(value,key)