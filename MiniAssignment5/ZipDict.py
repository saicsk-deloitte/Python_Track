'''list1 = ["Netflix", "Hulu", "Sling", "Hbo"]
list2 = [198, 166, 237, 125]
zipped_lst = zip(list1,list2)
dict = {}
for i in (zipped_lst):
    dict[i[0]] = i[1]
print(dict)'''

#Approach 2:
lst1=["Netflix", "Hulu", "Sling", "Hbo"]
lst2=[198, 166, 237, 125]
output=dict(zip(lst1,lst2))
print(output)