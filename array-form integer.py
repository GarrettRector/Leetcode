class Solution(object):
    def addToArrayForm(self, num, k):
        string = ''.join(str(i) for i in num)
        string = str(int(string) + k)
        return string


if __name__ == "__main__":
    s = Solution()
    print(s.addToArrayForm([1, 2, 0, 0], 34))
