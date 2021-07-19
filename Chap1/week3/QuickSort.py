import numpy as np

count = 0

class QuickSort():
    def __init__(self, nums):
        self.nums = nums

    def easyWay(self, left, right):
        n = right - left + 1
        if n < 2:
            return
        global count
        count += n - 1
        ans = [None for i in range(n)]
        start, end = 0, n - 1
        mid = left + n//2
        pivot = [self.nums[left], self.nums[right], self.nums[mid]]
        pivot.sort()
        if self.nums[right] == pivot[1]:
            self.nums[right], self.nums[left] = self.nums[left], self.nums[right]
        if self.nums[mid] == pivot[1]:
            self.nums[left], self.nums[mid] = self.nums[mid], self.nums[left]
        for i in range(left + 1, right + 1):
            if self.nums[i] > self.nums[left]:
                ans[end] = self.nums[i]
                end -= 1
            else:
                ans[start] = self.nums[i]
                start += 1
        pivot = left + start
        ans[start] = self.nums[left]
        self.nums[left:right+1] = ans
        self.easyWay(left, pivot - 1)
        self.easyWay(pivot + 1, right)
        return

    def In_place(self, left, right):
        global count
        n = right - left + 1
        if n:
            count += n - 1
        if n < 2:
            return
        i,j = left + 1, left + 1
        mid = (right + left) //2
        pivot = [self.nums[left], self.nums[right], self.nums[mid]]
        pivot.sort()
        self.nums[right], self.nums[left] = self.nums[left], self.nums[right]
        """
        if self.nums[mid] == pivot[1] and pivot[0] < self.nums[mid] < pivot[2]:
            self.nums[left], self.nums[mid] = self.nums[mid], self.nums[left]
        elif self.nums[right] == pivot[1] and pivot[0] < self.nums[right] < pivot[2]:
            self.nums[right], self.nums[left] = self.nums[left], self.nums[right]
        """
        while j != right + 1:
            while j != right and i == j and self.nums[i] < self.nums[left]:
                i += 1
                j += 1
            if j == right + 1:
                break
            if self.nums[j] < self.nums[left]:
                self.nums[j], self.nums[i] = self.nums[i], self.nums[j]
                i += 1
                j += 1
            else:
                j += 1

        pivot = i - 1
        #if self.nums[pivot] < self.nums[left]:
        self.nums[left], self.nums[pivot] = self.nums[pivot], self.nums[left]
        self.In_place(left, pivot - 1)
        self.In_place(pivot + 1, right)
        return

    def randomPivot(self, left, right):
        n = right - left + 1
        if n < 2:return
        pivot = np.random.randint(left,right + 1)

        i, j = left, right

        while i <= j:
            while i <= j and self.nums[i] < self.nums[pivot]:
                i += 1
            if  self.nums[i] >= self.nums[pivot]:
                self.nums[i], self.nums[pivot] = self.nums[pivot], self.nums[i]
                pivot = i
                i += 1
            while i <= j and self.nums[j] > self.nums[pivot]:
                j -= 1
            if self.nums[j] <= self.nums[pivot]:
                self.nums[j], self.nums[pivot] = self.nums[pivot], self.nums[j]
                pivot = j
                j -= 1
        self.randomPivot(left, pivot - 1)
        self.randomPivot(pivot + 1, right)

        return

#np.random.seed(10)
start, end = 1, 10000
nums = [i for i in range(start, end + 1)]
nums = np.loadtxt('QuickSort.txt')
#nums = np.loadtxt('1.txt',dtype=int)
nums = list(nums)
#np.random.shuffle(nums)

import time

a = nums.copy()
QS = QuickSort(a)
tic = time.time()
#QS.easyWay(0, end - start)
toc = time.time()
#print(toc - tic)

b = nums.copy()
QS = QuickSort(b)
tic = time.time()
QS.In_place(0,end - start)
toc =time.time()
print(count)
print(toc - tic)

c = nums.copy()
QS = QuickSort(c)
tic = time.time()
#QS.randomPivot(0,end - start)
toc =time.time()
print(toc - tic)
#print(c)

nums