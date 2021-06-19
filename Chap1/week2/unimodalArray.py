"""
You are a given a unimodal array of n distinct elements, meaning that its entries are
in increasing order up until its maximum element, after which its elements are in decreasing order.
Give an algorithm to compute the maximum element that runs in O(log n) time.
"""
import numpy as np
def findPeak(nums):
    n = len(nums)
    mid = n // 2
    if nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
        return nums[mid]
    elif nums[mid - 1] <= nums[mid] <= nums[mid + 1]:
        return findPeak(nums[mid:n])
    else:
        return findPeak(nums[0:mid])

nums = []
n = 1000
loc = 234
for i in range(loc):
    nums.append(i)
for i in range(n - loc):
    nums.append(loc - i)

print(findPeak(nums))
