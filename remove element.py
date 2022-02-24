class Solution:
    def removeElement(self, nums, val):
        nums[:] = [x for x in nums if x != val]
        return len(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.removeElement([3, 2, 2, 3], 3))
