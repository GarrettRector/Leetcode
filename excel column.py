class Solution(object):
    def titleToNumber(self, columnTitle):
        o = 0
        for i in columnTitle:
            o = o * 26 + ord(i) - 64
        return o


if __name__ == "__main__":
    s = Solution()
    s.titleToNumber("AB")
