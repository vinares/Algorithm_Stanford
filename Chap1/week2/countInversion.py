import numpy as np
def merge_and_count(nums):
    n = len(nums)
    if n < 2:
        return nums, 0
    a, ai = merge_and_count(nums[0:n//2])
    b, bi = merge_and_count(nums[n//2:n])
    count = ai + bi
    c = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            count += len(a) - i
            j += 1
    c += a[i::]
    c += b[j::]
    return c, count

nums = np.loadtxt('numbers.txt')
nums = list(nums)
print(merge_and_count(nums)[1])