class Solution:
    def runningSum(self, nums):
        return [sum(nums[:i]) + num for i, num in enumerate(nums)]
    
    
if __name__ == "__main__":
    s = Solution()
    s.runningSum([1, 2, 3, 4])
