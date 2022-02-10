class Solution:
    def addDigits(self, number):
        number = str(number)
        done = False
        sum_ = None
        while not done:
            n = [int(num) for num in number]
            sum_ = sum(n)
            number = str(sum_)
            if sum_ < 10:
                done = True
        return sum_


if __name__ == "__main__":
    s = Solution()
    s.addDigits(38)
