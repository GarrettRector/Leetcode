class Solution(object):
    def addDigits(self, number):
        number = str(number)
        done = False
        while not done:
            n = [int(num) for num in number]
            print(n)
            sum_ = sum(n)
            number = str(sum_)
            if sum_ < 10:
                done = True
        return sum_
        
