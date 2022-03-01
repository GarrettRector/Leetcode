class Solution(object):
    def fizzBuzz(self, n):
        r = []
        while n:
            if n % 3 == 0 and n % 5 == 0:
                r.append("FizzBuzz")
            elif n % 3 == 0:
                r.append("Fizz")
            elif n % 5 == 0:
                r.append("Buzz")
            else:
                r.append(str(n))
            n -= 1
        return r[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.fizzBuzz(15))
