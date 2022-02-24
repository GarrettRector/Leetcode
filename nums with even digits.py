class Solution(object):
    def findNumbers(self, nums):
        ans = [num for num in nums if len(str(num)) % 2 == 0]
        return len(ans)


if __name__ == "__main__":
    nums = [12, 345, 2, 6, 7896]
    Solution().findNumbers(nums)
