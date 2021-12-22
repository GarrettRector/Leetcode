class Solution:
    def intToRoman(self, num: int):
        symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        i, res = 0, ""

        while num > 0:
            while num >= value[i]:
                num -= value[i]
                res += symbol[i]
            i += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(99))
