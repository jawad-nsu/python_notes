# Arrays (called lists in python)
arr = [1, 2, 3]
print(arr)

# Arrays in python are dynamic arrays
# Can be used as a stack
arr.append(4)
print(arr)

arr.append(5)
print(arr)

arr.pop()
print(arr)

# since technically it's an array 
# and not a stack, we can insert into the middle
# unlike pushing and popping, it's O(n) time complexity 
arr.insert(1,7)
print(arr)

# Constant time operation 
arr[0] = 0
print(arr)

# Initialize arr of size n with default value of 1
n = 5
arr = [1] * n
print(arr)
print(len(arr))

# Careful: -1 is not out of bounds,
# it's the last value
arr = [1, 2, 3]
print(arr[-1])

# Indexing -2 is the second to last value, etc
print(arr[-2])

# Sublists (aka slicing)
arr = [1, 2, 3, 4]
print(arr[1:3]) #[2, 3] from index 1 to index 3, but not including index 3

# Similar to for-loop ranges
# last index is non-recursive
print(arr[0:4])

# Unpacking
# takes the individual elements of an array
# and assign them to variables
# can be very useful when we go through a list of pairs
a, b, c = [1, 2, 3]
print(a, b, c)

