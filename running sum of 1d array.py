class Solution:
    def runningSum(self, nums):
        ans = []
        for i, num in enumerate(nums):
            ans.append(sum(nums[:i]) + num)
        return ans
    
    
if __name__ == "__main__":
    s = Solution()
    s.runningSum([1, 2, 3, 4])
