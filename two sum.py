class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for n in range(i+1, len(nums)):
                if nums[i] + nums[n] == target:
                    return [i, n]
