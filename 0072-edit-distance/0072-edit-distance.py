class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        lev = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            lev[i][0] = i
        for i in range(n + 1):
            lev[0][i] = i
        for i, a_i in enumerate(word1):
            for j, b_j in enumerate(word2):
                if a_i == b_j:
                    lev[i + 1][j + 1] = lev[i][j]
                else:
                    lev[i + 1][j + 1] = min(lev[i][j + 1], lev[i + 1][j], lev[i][j]) + 1
        return lev[-1][-1]            
