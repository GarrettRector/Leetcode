class Solution:
    def missingNumber(self, nums):
        numbers = list(range(len(nums)+1))
        for num in numbers:
            if num not in nums:
                return num


if __name__ == "__main__":
    s = Solution()
    s.missingNumber([3, 0, 1])
