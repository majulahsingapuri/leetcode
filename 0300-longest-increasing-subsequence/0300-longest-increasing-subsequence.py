class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1] * length
        curMax = 1
        
        for i in range(len(nums) - 2, -1, -1):
            vals = [1]
            for j in range(i + 1, length):
                if nums[i] < nums[j]:
                    vals.append(dp[j] + 1)
            dp[i] = max(vals)
            curMax = max(curMax, dp[i])

        return curMax