class NestedList:
    def Nested(self,list1,list2):
        for i in range(len(list2)):
            list1[2][1][2].append(list2[i])
        print(list1)
l1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
l2=["h", "i", "j"]
nested_list=NestedList()
nested_list.Nested(l1,l2)


#Approach_2:
#l1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
#l2=['h','i','j']
#l1[2][1][2].extend(l2)
#print(l1)