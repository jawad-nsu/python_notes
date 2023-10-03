# Strings are similar to arrays
# we can slice them
s = "abc"
print(s[0:2])

# But they are immutable
s[0] = "A" # this will thrown an error

# updating string will create a new string
# appending `def` to the end of the string will create a new string
# string modification is considered n time operation 
s += "def"
print(s)