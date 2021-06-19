"""
You are given a sorted (from smallest to largest) array A of n distinct integers which can be positive, negative, or zero.
You want to decide whether or not there is an index i such that A[i] = i.
Design the fastest algorithm that you can for solving this problem.
"""

import numpy as np
def findEqual(nums):
    n = len(nums)
    left, right = 0, n - 1
    mid = (right - left) // 2
    while left <= right and mid > 0:
        mid = (right - left) // 2 + left
        if nums[mid] == mid:
            return True
        elif nums[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
    return False

def bruteForce(nums):
    n = len(nums)
    for i in range(n):
        if nums[i] == i:
            return True
    return False

n = 10000
np.random.seed(10)
nums = np.random.randint(-n, n, n)
nums.sort()
print(findEqual(nums))
print(findEqual(nums) == bruteForce(nums))