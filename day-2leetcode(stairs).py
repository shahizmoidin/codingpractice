class Solution(object):
    def climbStairs(self, n):
        f1=0
        f2=1
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            for i in range(n):
                f3=f1+f2
                f1=f2
                f2=f3
            return f3
