import numpy as np
class DSelection:
    def DS(self, nums, i):
        n = len(nums)
        if n < 2:
            return nums[0]
        medians = []
        for j in range(n//5):
            medians.append(list(nums[5 * j:5 * j+5]))
        if n % 5:
            medians.append(list(nums[(n // 5) * 5:n]))
        median_each = []
        for lst in medians:
            lst.sort()
            median_each.append(lst[len(lst)//2])

        median = self.DS(median_each, len(median_each)//2)
        for j in range(n):
            if nums[j] == median:
                nums[0], nums[j] = nums[j], nums[0]
        j, k = 1, 1
        while k < n:
            while k < n and j == k and nums[j] < median:
                k += 1
                j += 1
            if k >= n:
                break
            if nums[k] >= median:
                k += 1
            else:
                nums[k], nums[j] = nums[j], nums[k]
                j += 1
                k += 1

        pivot = j - 1

        nums[pivot], nums[0] = nums[0],  nums[pivot]
        if j == i:
            return nums[pivot]
        elif j > i:
            return self.DS(nums[0:pivot], i)
        else:
            return self.DS(nums[pivot + 1:n], i - j)

nums = np.arange(1,102)
np.random.shuffle(nums)
ans = DSelection().DS(nums,50)
print(ans)