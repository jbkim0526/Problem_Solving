from copy import deepcopy

d = {1:set([1,2,3])}

p = deepcopy(d)

p[1].add(4)

print(d,p)