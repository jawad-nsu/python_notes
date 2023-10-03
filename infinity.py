# Max / Min Int
float("inf")
float("-inf")

# Python numbers are infinite so they never overflow
import math
print(math.pow(2,200))

# but still less than infinity
print(math.pow(2, 200) < float("inf"))