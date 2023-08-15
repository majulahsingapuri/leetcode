class Solution:
    def climbStairs(self, n: int) -> int:
        x0 = 1
        x1 = 1
        y = 1
        
        for _ in range(n-1):
            y = x0 + x1
            x0 = x1
            x1 = y
        return y
            