given_list = [-1000, 500, -600, 700, 5000, -90000, -17500]
output = list(map(lambda x: abs(x), (filter(lambda x: x < 0, map(lambda x: x, given_list)))))
print(output)