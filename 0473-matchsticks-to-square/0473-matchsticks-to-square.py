class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        target = sum(matchsticks) / 4
        if target != int(target):
            return False

        sides = [0] * 4

        def backtrack(i):
            if i >= len(matchsticks):
                return True
            
            for side in range(4):
                sides[side] += matchsticks[i]
                if sides[side] <= target and backtrack(i + 1): return True
                sides[side] -= matchsticks[i]
            return False
    
        return backtrack(0)
        