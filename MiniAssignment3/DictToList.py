given_dict = {'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
print("Given dictionary is : " + str(given_dict))
result = []
for key, val in given_dict.items():
    result.append([key] + val)
print("Converted list is : " + str(result))