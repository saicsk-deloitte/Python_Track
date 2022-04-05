class StringClass:

    def __init__(self, string):
        self.string = string

    def length(self):
        return len(self.string)

    def converttolist(self):
        return list(self.string)


class PairsPossible(StringClass):
    def pairs(self, list2):
        possible = [(a, b)
                    for index, a in enumerate(list2)
                    for b in list2[index + 1:]]
        return possible


class SearchCommonElements(StringClass):
    def common(self, str2, string):
        removed_is = list(set(str2) & set(string))
        print(removed_is)


class EqualSumPairs():
    def count(self, res_list):
        lst = []
        for tup in res_list:
            sum = 0
            for i in tup:
                sum += int(i)
            lst.append(sum)
        print('sum which is not equal to sum of other pairs')
        print(set(lst))
        print(len(set(lst)))


string = input("Enter a string :")
ans1 = StringClass(string)
print(ans1.length())
print(ans1.converttolist())

sc_list = ans1.converttolist()
ans2 = PairsPossible(ans1)
result = ans2.pairs(sc_list)
print(result)

st2 = input("Enter a string :")

ans3 = SearchCommonElements(ans1)
ans3.common(st2, string)

ans4 = EqualSumPairs()
ans4.count(result)
