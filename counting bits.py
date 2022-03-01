class Solution(object):
    def countBits(self, n):
        return [format(i, 'b').count('1') for i in range(n + 1)]


if __name__ == "__main__":
    s = Solution()
    print(s.countBits(2))
