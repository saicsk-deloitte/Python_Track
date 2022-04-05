class dictionary:
    def mapDictionary(self,Key,Value):
        result = {Key[i]:Value[i] for i in range(len(Key))}
        print(result)
keys =["Ten", "Twenty", "Thirty"]
value = [10,20,30]
Obj = dictionary()
Obj.mapDictionary(keys,value)