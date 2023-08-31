class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[-1])

        if height == 0 or width == 0:
            return 0

        perimeter = 0

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    # top
                    if (i - 1 >= 0 and grid[i-1][j] == 0) or i == 0:
                        perimeter += 1
                    # bottom
                    if (i + 1 < height and grid[i+1][j] == 0) or i == height - 1:
                        perimeter += 1
                    # left
                    if ( j - 1 >= 0 and grid[i][j-1] == 0 ) or j == 0:
                        perimeter += 1
                    # right
                    if ( j + 1 < width and grid[i][j+1] == 0 ) or j == width - 1:
                        perimeter += 1

        return perimeter