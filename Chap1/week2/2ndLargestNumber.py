"""
You are given as input an unsorted array of n distinct numbers, where n is a power of 2.
Give an algorithm that identifies the second-largest number in the array, and that uses
at most   n + log(n) - 2   comparisons.
"""

import numpy as np
def divideAndConquer(nums):
    count = 0
    def find2nd(nums):
        nonlocal count
        n = len(nums)
        if n == 2:
            count += 1
            return (min(nums), max(nums))

        A = find2nd(nums[0:n // 2])
        B = find2nd(nums[n // 2:n])
        count += 1
        return (min(A[1], B[1]), max(A[1], B[1]))
    return find2nd(nums)[0], count

n = 10
np.random.seed(10)
nums = np.random.randn(2 ** n)
sortedlist = nums.copy()
sortedlist.sort()
a = divideAndConquer(nums)
print(a[0] == sortedlist[-2])
print(a[1] <= n + 2 ** n - 2)