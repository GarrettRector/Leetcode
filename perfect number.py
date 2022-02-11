import math


class Solution:
    def checkPerfectNumber(self, num):
        s = 1 + sum(i + num // i for i in range(2, int(math.sqrt(num)) + 1) if num % i == 0)
        return num == s if num > 1 else False


if __name__ == "__main__":
    s = Solution()
    s.checkPerfectNumber(30402457)
