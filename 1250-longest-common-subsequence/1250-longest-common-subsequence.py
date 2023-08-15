import numpy as np

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        result = np.zeros((len(text1) + 1, len(text2) + 1), dtype=int)
        for i, a_i in enumerate(text1):
            for j, b_j in enumerate(text2):
                if a_i == b_j:
                    result[i + 1, j + 1] = 1 + result[i, j]
                else:
                    result[i + 1, j + 1] = max(result[i, j + 1], result[i + 1, j])
        return result[-1, -1]