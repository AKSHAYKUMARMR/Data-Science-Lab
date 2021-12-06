tup=((1,"one"),(2,"two"),(3,"three"),(4,"four"))
print(tup)
((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'))
dct=dict(map(reversed,tup))
print(dct)
{'one': 1, 'two': 2, 'three': 3, 'four': 4}
