# hashsets are useful because we can search 
# for items in constant time, and also insert
# values in constant time

mySet = set()

# also there are no duplicates
mySet.add(1)
mySet.add(2)
mySet.add(2)
print(mySet) # {1, 2}
print(len(mySet)) # 2

# we can check if an item exists inside the hashmap 
# without any function by using the in operator
print(1 in mySet)
print(2 in mySet)
print(3 in mySet)

# we can also remove values in constant time
mySet.remove(2)
print(2 in mySet)

# list to set
print(set([1, 2, 3]))

# Set comprehension
mySet = { i for i in range(5)}
print(mySet)
