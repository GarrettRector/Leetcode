class Solution(object):
    def runningSum(self, nums):
        ans = []
        for i, num in enumerate(nums):
            ans.append(sum(nums[:i]) + num)
        return ans
