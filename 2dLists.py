# 2-D lists
arr = [[0] * 4 for i in range(3)]
print(arr)

# This won't work
# Although this will create a 3 by 4 
# list, all the arrays inside the inner array
# will be idential, so any modifications we
# make to the condition of inner array will
# impact all of the inner arrays 
arr = [[0] * 4] * 3
print(arr)