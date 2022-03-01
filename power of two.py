class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        if n == 1:
            return True
        elif n % 2 == 0:
            return self.isPowerOfTwo(n / 2)


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfTwo(217))
