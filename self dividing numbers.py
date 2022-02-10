class Solution:
    def selfDividingNumbers(self, left, right):
        ans = []
        for i in range(left, right + 1):
            divisions = []
            for char in str(i):
                try:
                    if i % int(char) == 0:
                        divisions.append(True)
                    else:
                        divisions.append(False)
                except ZeroDivisionError:
                    divisions.append(False)
            if all(divisions):
                ans.append(i)
        return ans


if __name__ == '__main__':
    s = Solution()
    s.selfDividingNumbers(1, 22)
