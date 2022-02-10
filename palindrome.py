class Solution:
    def isPalindrome(self, x: str):
        y = False

        x = str(x)
        if x[0] == "-":
            y = True
            x = x[1:]

        solution = "".join(x[len(x) - i - 1] for i in range(len(str(x))))

        if y:
            solution = "-" + solution

        return solution == x


if __name__ == "__main__":
    s = Solution()
    s.isPalindrome("racecar")
