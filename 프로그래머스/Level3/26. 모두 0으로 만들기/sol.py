from collections import defaultdict

def solution(a, edges):
    if sum(a) != 0:
        return -1
        
    answer = 0
    node_dict = defaultdict(set)
    
    for n1,n2 in edges:
        node_dict[n1].add(n2)
        node_dict[n2].add(n1)
    
    leaf_nodes = []

    for node,adj_nodes in node_dict.items():
        if len(adj_nodes) == 1:
            leaf_nodes.append(node)

    while len(leaf_nodes) > 0:
        leaf_candidates = set()

        for leaf_node in leaf_nodes:
            if len(node_dict[leaf_node]) == 0:
                return -1 if a[leaf_node] else answer

            adj_node = list(node_dict[leaf_node])[0]
            if a[leaf_node] != 0:
                a[adj_node] += a[leaf_node]
                answer += abs(a[leaf_node])
                a[leaf_node] = 0
            
            node_dict[adj_node].remove(leaf_node)
            node_dict[leaf_node].remove(adj_node)
            leaf_candidates.add(adj_node)

        leaf_nodes = []

        for candidate in leaf_candidates:
            if len(node_dict[candidate]) == 1:
                leaf_nodes.append(candidate)

    return -1 if any(a) else answer 

print(solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]))
#print(solution([0, 1, 0], [[0, 1], [1, 2]]))
