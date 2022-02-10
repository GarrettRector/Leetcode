class Solution:
    def reverse(self, x: int) -> int:
        
        y = False

        x = str(x)
        if x[0] == "-":
            y = True
            x = x[1:]

        solution = "".join(x[len(x)-i-1] for i in range(len(str(x))))

        if y:
            solution = "-" + solution

        solution = int(solution)
        if solution > 2147483650 or solution < -2147483650:
            solution = 0
        return solution


if __name__ == "__main__":
    s = Solution()
    s.reverse(12345)