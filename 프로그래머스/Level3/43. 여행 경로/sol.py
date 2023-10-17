from collections import defaultdict

def solution(tickets):
    answer = []
    n = len(tickets)
    adj_airport = defaultdict(list)
    for a,b in tickets:
        adj_airport[a].append(b)

    def track(cur_airport,path):
        if len(path) >= n+1:
            answer.append(path.copy())
            return
        for next_airport in adj_airport[cur_airport]:
            if len(path) == 1:
                print(next_airport)
                print(adj_airport[cur_airport])
            adj_airport[cur_airport].remove(next_airport)
            path.append(next_airport)
            track(next_airport,path)
            adj_airport[cur_airport].append(next_airport)
            path.pop()
        return
        
    track("ICN",["ICN"])
    print(answer)
    answer.sort()
    return answer[0]


#print(solution(	[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
#print(solution([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]))