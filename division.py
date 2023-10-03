# Division is decimal by default
print(5 / 2)

# Double slash rounds down
print(5 // 2)

# CAREFUL: most languages round toward 0 by 
# default so negative numbers will be round down
print(-3 // 2)

# A workaround for rounding towards zero is to
# use decimal division and then convert to int.
print(int(-3 / 2))