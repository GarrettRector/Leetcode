class Solution(object):
    def plusOne(self, digits):
        for i, digit in enumerate(digits):
            digits[i] = str(digit)
        return [int(i) for i in str(int("".join(digits)) + 1)]


if __name__ == "__main__":
    s = Solution()
    s.plusOne([4, 3, 2, 1])
