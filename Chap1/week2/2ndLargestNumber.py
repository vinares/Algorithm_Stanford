"""
You are given as input an unsorted array of n distinct numbers, where n is a power of 2.
Give an algorithm that identifies the second-largest number in the array, and that uses
at most   n + log(n) - 2   comparisons.
"""
from collections import defaultdict
from lib2to3.pytree import HUGE
import numpy as np
def divideAndConquer(nums):
    ht = defaultdict(list)
    def find1st(nums):
        n = len(nums)
        if n == 0:
            return -1, 0
        if n == 1:
            return nums[0], 0
        if n == 2:
            if nums[0] > nums[1]:
                ht[nums[0]].append(nums[1])
                return nums[0], 1
            else:
                ht[nums[1]].append(nums[0])
                return nums[1], 1
        A, a = find1st(nums[0:n // 2])
        B, b = find1st(nums[n // 2:n])
        if A > B:
            ht[A].append(B)
            return A, a + b + 1
        else:
            ht[B].append(A)
            return B, a + b + 1
    M, c = find1st(nums)
    MM, cc= find1st(ht[M])
    return MM, c + cc


n = 100
np.random.seed(10)
nums = [i for i in range(1, n+1)]
np.random.shuffle(nums)
sortedlist = nums.copy()
sortedlist.sort()
a = divideAndConquer(nums)
assert a[0] == sortedlist[-2]
assert a[1] <= n + np.ceil(np.log2(n)) - 2
