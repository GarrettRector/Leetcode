class Solution(object):
    def findEvenNumbers(self, digits):
        n = len(digits)
        res = []

        for i in range(n):
            if digits[i] != 0:
                for j in range(n):
                    if j != i:
                        for k in range(n):
                            if digits[k] % 2 == 0 and k not in (i, j):
                                res.append(digits[i] * 100 + digits[j] * 10 + digits[k])

        res = list(set(res))
        res.sort()
        return res


if __name__ == "__main__":
    s = Solution()
    s.findEvenNumbers([2, 2, 8, 8, 2])
