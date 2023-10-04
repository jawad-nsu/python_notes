# tuples are like arrays but immutable

tup = (1, 2, 3)
print(tup)

# we can index them
print(tup[0])
print(tup[-1])

# Can't modify 
# tup[0] = 0

# we'll be mostly using tuples as key for 
# hash map / set 
myMap = { (1, 2): 3 }

# this tuple is our hashable key
print(myMap[(1, 2)])

# we can do the same thing for hashsets ofcourse
mySet = set()
mySet.add((1, 2))
# and use the tuple to search the hashSet
print((1, 2) in mySet)

# Lists can't be keys
myMap[[3, 4]] = 5