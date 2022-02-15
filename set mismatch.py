class Solution(object):
    def findErrorNums(self, nums):
        repeat = sum(nums) - sum(set(nums))
        expected = ((len(nums)) * (len(nums) + 1)) // 2
        missing = expected - sum(nums) + repeat
        return repeat, missing


if __name__ == "__main__":
    s = Solution()
    print(s.findErrorNums([2, 2]))
