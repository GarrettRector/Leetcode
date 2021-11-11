class Solution(object):
    def reverse(self, x):
        
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
            
        solution = int(solution)
        if solution > 2147483650:
            solution = 0
        elif solution < -2147483650:
            solution = 0
        
        return solution
