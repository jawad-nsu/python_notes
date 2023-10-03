# Sorting, by default will sort by ascending order
arr = [5, 4, 7, 3, 8]
arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)

# sort by default is in alphabetical order
arr = ['bob', 'alice', 'jane', 'doe']
arr.sort()
print(arr)

# Custom sort (by length of string)
arr.sort(key=lambda x: len(x))
print(arr)