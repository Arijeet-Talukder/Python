import copy
print('hello world')
c = [[1,2],[3,4]]
d = copy.deepcopy(c)
d[0].append(5)
print(id(c))
print(id(d))
print(id(c[0]))
print(id(d[0]))
print(c)
print(d) 
#mutable object: list, dict, set
#immutable object: int, float, str, tuple  