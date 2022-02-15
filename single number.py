class Solution:
    def singleNumber(self, nums):
        for num in set(nums):
            if nums.count(num) == 1:
                return num


if __name__ == "__main__":
    s = Solution()
    s.singleNumber([4, 1, 2, 1, 2])
