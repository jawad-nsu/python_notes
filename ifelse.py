# If statements don’t need parentheses or curly braces, 
# instead we use semicolon & indentation to indicate the block of code.

# else if is written as `elif`

n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2

print('n = ', n)