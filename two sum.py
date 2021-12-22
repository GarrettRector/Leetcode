class Solution:
    def twoSum(self, nums: list, target: int) -> list[int, int]:
        for i in range(len(nums)):
            for n in range(i+1, len(nums)):
                if nums[i] + nums[n] == target:
                    return [i, n]


if __name__ == "__main__":
    s = Solution()
    s.twoSum([3, 2, 4], 6)