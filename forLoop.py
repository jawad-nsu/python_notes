# Looping from i = 0 to i = 4
for i in range(5):
        print(i)

# here, we don't have to tell i to increment on every loop
# rather, i is going to be incremented by default

# Looping from i = 2 to i = 5
for i in range(2, 6):
        print(i)

# Looping from i = 5 to i = 2
for i in range(5, 1, -1):
        print(i)
# if we don't pass the -1 decrement as the third argument, 
# then by default it'll increment, we can even pass -2