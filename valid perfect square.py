class Solution(object):
    def isPerfectSquare(self, num):
        return int(num ** 0.5) == num ** 0.5


if __name__ == "__main__":
    s = Solution()
    print(s.isPerfectSquare(15))
