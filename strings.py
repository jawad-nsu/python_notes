# Strings are similar to arrays
# we can slice them
s = "abc"
print(s[0:2])

# But they are immutable
# s[0] = "A" # this will thrown an error

# updating string will create a new string
# appending `def` to the end of the string will create a new string
# string modification is considered n time operation 
s += "def"
print(s)

# valid numeric strings can be converted
print(int("123") + int("123"))

# And numbers can be converted to strings
print(str(123) + str(123))

# In rare cases you may need the ASCII value
# of a char
print(ord('a'))
print(ord('b'))
