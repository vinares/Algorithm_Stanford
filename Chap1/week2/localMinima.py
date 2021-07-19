"""
You are given an n by n grid of distinct numbers. A number is a local minimum if it is smaller than all of its neighbors.
(A neighbor of a number is one immediately above, below, to the left, or the right. Most numbers have four neighbors;
numbers on the side have three; the four corners have two.)
Use the divide-and-conquer algorithm design paradigm to compute a local minimum with only O(n) comparisons between pairs of numbers.
(Note: since there are n*n numbers in the input, you cannot afford to look at all of them.
Hint: Think about what types of recurrences would give you the desired upper bound.)
"""

import numpy as np

def localMinima(nums):
    n = len(nums)
    if check(nums, 0, 0):
        return (0, 0)
    if check(nums, 0, n - 1):
        return (0, n - 1)
    if check(nums, n - 1, 0):
        return (n - 1, 0)
    if check(nums, n - 1, n - 1):
        return (n - 1, n - 1)
    for i in range(1, n-1):
        if check(nums, 0, i):
            return (0,i)
        if check(nums, n - 1, i):
            return (n-1,i)
        if check(nums, i, 0):
            return (i,0)
        if check(nums, i, n - 1):
            return (i,n-1)
        if check(nums, n//2, i):
            return (n//2,i)
        if check(nums, i, n//2):
            return (i,n//2)
    if n < 3:
        return (-1, -1)
    A, B = nums[1:n//2,1:n//2], nums[1:n//2, n//2 + 1: n - 1]
    C, D = nums[n//2+1:n - 1], nums[n//2 + 1:n -1,n//2+1:n-1]
    if localMinima(A) != (-1, -1):
        return localMinima(A)
    if localMinima(B) != (-1, -1):
        return localMinima(B)
    if localMinima(C) != (-1, -1):
        return localMinima(C)
    if localMinima(D) != (-1, -1):
        return localMinima(D)
    return (-1, -1)
count = 0
def check(nums, x, y):
    aj = []
    n = len(nums)
    global count
    if x!= 0:
        aj.append((x - 1, y))
    if x!=n-1:
        aj.append((x+1,y))
    if y!=0:
        aj.append((x,y-1))
    if y!=n-1:
        aj.append((x,y+1))
    flag = True
    for point in aj:
        count += 1
        if nums[x][y] > nums[point[0]][point[1]]:
            flag = False
    return flag


np.random.seed(467)
n = 100
for i in range(10000):
    matrix = np.random.randint(0,100,(n,n))
    localMinima(matrix)
print(count)