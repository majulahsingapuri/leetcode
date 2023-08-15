class Solution:
    def fib(self, n: int) -> int:
        if 0 <= n <= 1:
            return n
        x0 = 0
        x1 = 1
        
        
        for _ in range(n-1):
            y = x0 + x1
            x0 = x1
            x1 = y
        return y