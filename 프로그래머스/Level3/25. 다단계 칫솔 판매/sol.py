def print_tree(node):
    print(node.name)
    if len(node.child) == 0:
        return 
    for child_node in node.child:
        print_tree(child_node) 


from collections import defaultdict

class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.child = []

def solution(enroll, referral, seller, amount):
    answer = []

    node_dict = {}
    node_dict["-"] = Node("root")
    profit_dict = defaultdict(int)
    for i in range(len(enroll)):
        name = enroll[i]
        recommender = referral[i]
        parent = node_dict[recommender]
        cur_node = Node(name,parent)
        parent.child.append(cur_node)
        node_dict[name] = cur_node

    for i in range(len(seller)):
        money = amount[i]*100
        cur_node = node_dict[seller[i]]

        while money > 0 and cur_node.name != "root":
            share_profit = int(money*0.1)
            profit_dict[cur_node.name] += money-share_profit
            money = share_profit
            cur_node = cur_node.parent

    for name in enroll:
        answer.append(profit_dict[name])

    return answer



print(solution(	["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))