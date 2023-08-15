class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        x0 = 0
        x1 = 1
        x2 = 1
        
        for _ in range(n-2):
            y = x0 + x1 + x2
            x0 = x1
            x1 = x2
            x2 = y
        return y