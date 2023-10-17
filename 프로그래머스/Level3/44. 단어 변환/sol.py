from collections import defaultdict
from math import inf
def solution(begin, target, words):
    total_words = words + [begin]
    total_words_len = len(total_words)
    n = len(begin)
    adj_words = defaultdict(set)
    scores = defaultdict(int)

    for i in range(total_words_len):
        scores[total_words[i]] = inf
        for j in range(i):
            count = 0
            cur_word = total_words[i]
            next_word = total_words[j]
            for k in range(n):
                if cur_word[k] == next_word[k]:
                    continue 
                count += 1
            if count == 1:
                adj_words[next_word].add(cur_word)
                adj_words[cur_word].add(next_word)

    l = [begin]
    scores[begin] = 0
    
    while len(l) > 0:
        cur_word = l.pop()
        next_score = scores[cur_word] + 1
        for adj_word in adj_words[cur_word]:
            if next_score < scores[adj_word]:
                scores[adj_word] = next_score
                l.append(adj_word)

    return scores[target]




#print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))