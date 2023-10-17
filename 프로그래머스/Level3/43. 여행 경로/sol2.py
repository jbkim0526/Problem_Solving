from collections import defaultdict
from copy import deepcopy

def solution(tickets):
    answer = []
    n = len(tickets)
    adj_airport = defaultdict(list)
    for a,b in tickets:
        adj_airport[a].append(b)

    def track(cur_airport, adj_airport, path):
        if len(path) >= n+1:
            answer.append(path.copy())
            return
        for next_airport in adj_airport[cur_airport]:
            new_adj_airport = deepcopy(adj_airport)
            new_adj_airport[cur_airport].remove(next_airport)
            path.append(next_airport)
            track(next_airport,new_adj_airport,path)
            path.pop()
        return

    track("ICN",adj_airport,["ICN"])
    answer.sort()
    return answer[0]


#print(solution(	[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
#print(solution([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]))