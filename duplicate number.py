class Solution:
    def findDuplicate(self, nums):
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i], 0) + 1

        for key, val in dic.items():
            if val >= 2:
                return key


if __name__ == "__main__":
    s = Solution()
    s.findDuplicate([1, 3, 4, 2, 2])
