def myFunc(n, m):
    return n * m

print(myFunc(3, 4))

# nested functions have access to variables in
# outer function
def outer(a, b):
    c = "c"

    def inner():
        return a + b + c
    
    return inner()

print(outer("a", "b"))

# Can modify objects but not reassign variables
# unless using nonlocal keyword
# let's take this `arr` being passed as an arg 
# for example, if we change the arr inside the 
# nested function, the change will prevail outside as well
# but the same cannot be said about the variable `val`
# if we reassign it's value, it won't prevail outside
# of the inner function, if we want the changes to persist
# outside the inner function, we can use nonlocal keyword
def double(arr, val):
    def helper():
        # Modifying array works
        for i, n in enumerate(arr):
            arr[i] *= 2
        
        # will only modify val in the helper scope
        # val *= 2

        # this will modify val outside helper scope
        nonlocal val
        val *= 2
    helper()
    print(arr, val)

nums = [1, 2]
val = 3
double(nums, val)