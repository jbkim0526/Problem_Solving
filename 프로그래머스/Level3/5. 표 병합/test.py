d = {}
l = set([0,1])
r = set([2,3])
d[0] = l 
d[1] = l
d[2] = r
d[3] = r

s2 = d[2]
s1 = d[0]
for elem in s2:
    s1.add(elem)
    d[elem] = s1 


print(d)