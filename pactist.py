import functools

factorail = [5,4,3,2,1]
results = functools.reduce(lambda x, y,:x * y, factorail)
print(results)