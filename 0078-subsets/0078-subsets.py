class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        memo = {}

        subset = []

        def dfs(i):
            if memo.get(str(subset)):
                return
            if i >= len(nums):
                memo[str(subset)] = True
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
