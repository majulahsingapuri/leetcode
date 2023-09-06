class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        res = []
        cur = ""
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(i):
            nonlocal cur
            if i >= len(digits):
                res.append(cur)
                return
            for c in mapping[digits[i]]:
                cur = cur + c
                dfs(i + 1)
                cur = cur[:-1]

        dfs(0)
        return res
                  