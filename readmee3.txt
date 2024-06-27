day 2

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2

        f1=1
        f2=2
        for i in range(3,n+1):
            f3=f1+f2
            f1=f2
            f2=f3
        return f2