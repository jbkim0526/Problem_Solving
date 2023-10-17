from collections import defaultdict
from copy import deepcopy

def solution(info, edges):
    adj_nodes = defaultdict(set)
    for n1, n2 in edges:
        adj_nodes[n1].add(n2)
        adj_nodes[n2].add(n1)
    
    def update_dict(d, delete_node, target_node):
        for node in d[delete_node]:
            if node == target_node:
                continue
            d[node].add(target_node)
            d[target_node].add(node)
            d[node].remove(delete_node)
        d[target_node].remove(delete_node)
        del d[delete_node]
        return d

    def track(adj_nodes, node, lamb, wolf):
        if not info[node]: 
            lamb += 1
        else: 
            wolf += 1
        if wolf >= lamb:
            return lamb 
        
        for adj_node in adj_nodes[node]:
            if info[adj_node]:
                continue
            new_adj_nodes = update_dict(deepcopy(adj_nodes),node,adj_node)
            return track(new_adj_nodes,adj_node,lamb,wolf)
        ans = []
        for adj_node in adj_nodes[node]:
            new_adj_nodes = update_dict(deepcopy(adj_nodes),node,adj_node)
            ans.append(track(new_adj_nodes,adj_node,lamb,wolf))
        if len(ans) == 0:
            return lamb
        return max(ans)

    return track(adj_nodes,0,0,0)

print(solution([0,0,0,0,0,0,0,0,0,0,0,0],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]	))