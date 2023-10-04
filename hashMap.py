
# HashMap (aka dict)
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)
print(len(myMap))

# just like in HashSet we can't have 
# duplicate keys in hashset, but we 
# can modify the value a key has
myMap["alice"] = 80 
print(myMap)

# we can also search if a key exists
# in a hashmap in constant time
print("alice" in myMap)
myMap.pop("alice")
print("alice" in myMap)

# initializing a hashmap
myMap2 = {"maria": 90, "carzone": 70}

# Dict comprehension
myMap = { i: 2*i for i in range(3) }
print(myMap)

# Looping through maps
myMap = { "alice": 90, "bob": 70}

# iterating through every item
for key in myMap:
    print(key, myMap[key])

# directly iterate through the list 
# of values if we don't need the key
for val in myMap.values():
    print(val)

# using unpacking, we can go through the items 
# of an map, which will give us both the key and
# the value
for key, val in myMap.items():
    print(key, val)