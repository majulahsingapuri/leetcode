class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        memo = [ [-1 for _ in range(COLS)] for _ in range(ROWS)]
        count = 0

        def dfs(i, j, parent):
            if not (0 <= i < ROWS) or not (0 <= j < COLS) or memo[i][j] != -1 or grid[i][j] == "0":
                return

            memo[i][j] = parent

            dfs(i + 1, j, (i, j))
            dfs(i - 1, j, (i, j))
            dfs(i, j + 1, (i, j))
            dfs(i, j - 1, (i, j))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and memo[i][j] == -1:
                    count += 1
                    dfs(i, j, (i, j))

        return count