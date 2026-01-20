marks={"parth": 31, "ram": 62, "hero": 33}

print(marks["parth"])   # 31

marks["newadded"] = 23
marks["parth"] = 99

print(marks)    # {'parth': 99, 'ram': 62, 'hero': 33, 'newadded': 23}

# funcs
myDict = {"a": 1, "b": 2, "c": 3}

print(myDict.keys())             # all keys
print(myDict.values())           # all values
print(myDict.items())            # all (key, value) pairs

myDict.update({"b": 20, "d": 4})  # add/update items
print(myDict)