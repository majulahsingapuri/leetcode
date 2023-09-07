class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        max_ = 0
        memo = [ [0 for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(i, j):
            if not (0 <= i < ROWS) or not (0 <= j < COLS) or memo[i][j] != 0 or grid[i][j] == 0:
                return 0

            memo[i][j] = 1

            return sum([
                dfs(i + 1, j),
                dfs(i - 1, j),
                dfs(i, j + 1),
                dfs(i, j - 1)
            ]) + 1

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and memo[i][j] == 0:
                    new = dfs(i, j)
                    if new > max_:
                        max_ = new

        return max_
        