strings = ["dab", "add","cab","fab","fee","bad","dad","bee","fed","bed","ebb","ace"]

R = 256

def msd_sort(strings):
    aux = [None]*(len(strings))
    return _msd_sort(strings,aux,0,len(strings)-1,0)

def charAt(string,d):
    return ord(string[d]) if d < len(string) else -1

def _msd_sort(strings,aux,lo,hi,d):

    if lo >= hi:
        return 

    counts = [0]*(R+2)

    for i in range(lo,hi+1):
        counts[charAt(strings[i],d)+2] += 1

    for i in range(1,R+2):
        counts[i] += counts[i-1]

    for i in range(lo,hi+1):
        aux[counts[charAt(strings[i],d)+1]] = strings[i]
        counts[charAt(strings[i],d)+1] += 1
    
    for i in range(lo,hi+1):
        strings[i] = aux[i]

    for r in range(R):
        _msd_sort(strings, aux, lo+counts[r], lo+counts[r+1]-1, d+1)
    
msd_sort(strings)

print(strings)



