import numpy as np

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = np.ones((m, n), dtype=int)
        for i in range(1, m):
            for j in range(1, n):
                matrix[i, j] = matrix[i - 1, j] +  matrix[i, j - 1]
        return matrix[-1, -1]