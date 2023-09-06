class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(i):
            if len(cur) >= k:
                res.append(cur.copy())
                return

            for j in range(i, n + 1):
                cur.append(j)
                dfs(j + 1)
                cur.pop()
        
        dfs(1)
        return res
        