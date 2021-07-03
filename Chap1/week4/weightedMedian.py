import numpy as np

class RSelection:
    def RS(self, nums, weight,hashtable,W,start,end):
        n = len(nums)
        if n < 2:
            return [nums[0]]

        left, right = start + 1, start + 1
        pivot = np.random.randint(start,end)
        nums[start], nums[pivot] = nums[pivot], nums[start]
        while right <= end:
            while right <= end and left == right and nums[left] < nums[start]:
                left += 1
                right += 1
            if right > end:
                break
            if nums[right] < nums[start]:
                nums[left], nums[right] = nums[right], nums[left]
                right += 1
                left += 1
            else:
                right += 1
        pivot = left - 1
        nums[pivot], nums[start] = nums[start], nums[pivot]

        sum_l, sum_r = 0, 0
        for i in range(0,pivot):
            sum_l += hashtable[nums[i]]
        for i in range(pivot + 1,n):
            sum_r += hashtable[nums[i]]
        if sum_r < W/2 and sum_l < W/2:
            return [nums[pivot]]
        elif pivot > 0 and sum_l == W/2:
            return [nums[pivot],nums[pivot - 1]]
        elif pivot < n and sum_r == W/2:
            return [nums[pivot], nums[pivot + 1]]
        elif sum_l > W/2:
            weight[pivot] += sum_r
            return self.RS(nums,weight,hashtable,W,start,pivot)
        else:
            weight[pivot] += sum_l
            return self.RS(nums,weight,hashtable,W,pivot,end)


start, end = 1,101
nums = np.arange(start,end)
weight = []
for i in range(start,end + 1):
    weight.append(np.random.randint(1,10))
np.random.shuffle(nums)

W = 0
hashtable = dict()
for i in range(len(nums)):
    W += weight[i]
    hashtable[nums[i]] = weight[i]

ans = RSelection().RS(nums,weight,hashtable,W,0, end - start - 1)
print(ans)