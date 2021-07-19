import numpy as np

class RSelection:
    def RS(self, nums, i):
        n = len(nums)
        if n < 2:
            return nums[0]
        pivot = np.random.randint(0,n - 1)
        nums[0], nums[pivot] = nums[pivot], nums[0]
        left, right = 1, 1
        while right < n:
            while right < n and left == right and nums[left] < nums[0]:
                left += 1
                right += 1
            if right == n:
                break
            if nums[right] > nums[0]:
                right += 1
            else:
                nums[right], nums[left] = nums[left], nums[right]
                right += 1
                left += 1
        nums[0], nums[left - 1] = nums[left - 1], nums[0]
        if left == i:
            return nums[left - 1]
        elif left < i:
            return self.RS(nums[left:n], i - left)
        else:
            return self.RS(nums[0:left - 1], i)

nums = np.arange(1,101)
np.random.shuffle(nums)
ans = RSelection().RS(nums,50)
print(ans)