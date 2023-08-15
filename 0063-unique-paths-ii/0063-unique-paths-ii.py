import numpy as np

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        matrix = np.ones((m, n), dtype=int)
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] == 1:
                    matrix[i, j] = 0
                elif i == 0 and j - 1 >= 0 and obstacleGrid[i][j - 1] == 1:
                    matrix[i, j:] = 0
                elif j == 0 and i - 1 >= 0 and obstacleGrid[i - 1][j] == 1:
                    matrix[i:, j] = 0
                elif i - 1 >= 0 and j - 1 >= 0:
                    matrix[i, j] = matrix[i - 1, j] +  matrix[i, j - 1]
        return matrix[-1, -1]