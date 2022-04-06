given_list = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
count_A = list(map(lambda x: x.count("A"), given_list))
count_a = list(map(lambda x: x.count("a"), given_list))
merge = list(map(lambda x, y: [x, y], count_a, count_A))
print(merge)