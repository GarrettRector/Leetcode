class Solution(object):
    def isPowerOfThree(self, n):
        if n == 0:
            return False
        if n == 1:
            return True
        elif n % 3 == 0:
            return self.isPowerOfThree(n / 3)


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfThree(18))