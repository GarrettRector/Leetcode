class Solution(object):
    def hammingWeight(self, n):
        string = list(str(n).replace("0", ''))
        return len(string)


if __name__ == "__main__":
    s = Solution()
    print(s.hammingWeight())
