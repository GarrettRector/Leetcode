class Solution:
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)


if __name__ == "__main__":
    s = Solution()
    s.containsDuplicate([1, 2, 3, 4, 1])
