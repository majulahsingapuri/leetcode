class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        q = deque([])
        visited = set()
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c, 0))

        while q:
            r, c, curtime = q.popleft()
            if (r, c) in visited:
                continue
            visited.add((r, c))
            grid[r][c] = 2
            time = max(time, curtime)
            for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                if 0 <= r + dr < ROWS and 0 <= c + dc < COLS and grid[r + dr][c + dc] == 1:
                    q.append((r + dr, c + dc, curtime + 1))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return time
        