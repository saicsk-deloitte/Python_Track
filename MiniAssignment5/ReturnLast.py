from functools import reduce
list = [1,2,3,5,4]
result = reduce(lambda x, y: x * y, list)
print(result)