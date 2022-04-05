class RenameDictionary:
    def update(self,dict):
        dict["location"]=dict.pop("city")
        print(dict)
given_Dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
rename = RenameDictionary()
rename.update(given_Dict)