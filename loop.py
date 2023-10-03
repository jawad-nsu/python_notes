# Loop through arrays
nums = [1, 2, 3]

# Using index
# for i in range(len(nums)):
#     print(nums[i])

# without index
# for n in nums:
#     print(n)

# with index and value
# for i, n in enumerate(nums):
#     print(i, n)

# Loop through mulitple arrays simultaneously
# with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)