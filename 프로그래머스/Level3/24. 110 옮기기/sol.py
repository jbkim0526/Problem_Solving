def kmp(word):
    table = [0,1,0]
    pattern = "110"
    results = [] 
    pidx = 0
    for idx in range(len(word)):
        while pidx > 0 and word[idx] != pattern[pidx] :
            pidx = table[pidx-1]
        if word[idx] == pattern[pidx]:
            if pidx == len(pattern)-1 :
                results.append(idx-len(pattern)+1)
                pidx = table[pidx]
            else:
                pidx += 1
    return results

def move(text,i,j):
    s = text[:j] +"110"+ text[j:]
    return s[:i+3]+s[i+6:]

def solution(s):
    answer = []

    for word in s:
      
        while True:
            index110 = word.rfind("110")
            if index110 == -1:
                break 

            s

        
        indices = kmp(word)
        print(indices)
        while len(indices) > 0:
            index111 = word.find("111")
            if index111 == -1:
                break 
            index110 = indices.pop()
            word = move(word,index110,index111)

        s = ""
        index_set = set(indices)
        for index in indices:
            index_set.add(index+1)
            index_set.add(index+2)

        for i in range(len(word)):
            if i in index_set:
                continue 
            s += word[i]
        
        s += "110"*len(indices)
        answer.append(s)
    return answer


print(solution(["1110","100111100","0111111010"]))