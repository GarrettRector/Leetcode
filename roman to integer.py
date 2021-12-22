class Solution:
    def romanToInt(self, s: str):
        r_sum = 0
        temp = 0
        rul = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for ch in s:
            ch_val = int(rul[ch])
            r_sum = r_sum + ch_val
            if temp < ch_val:
                r_sum -= temp * 2
            temp = ch_val
        return r_sum


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("IV"))
