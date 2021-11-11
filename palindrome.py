class Solution(object):
    def isPalindrome(self, x):
        y = False
        
        x = str(x)
        if x[0] == "-":
            y = True
            x = x[1:]
        
        solution = ""
        
        for i in range(len(str(x))):
            solution += x[len(x)-i-1]
        
        if y:
            solution = "-" + solution
        
        if solution == x:
            return True
        else:
            return False
