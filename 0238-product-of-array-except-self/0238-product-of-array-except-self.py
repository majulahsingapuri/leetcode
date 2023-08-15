class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans, pre, post = [1]*len(nums), 1, 1
        for i in range(len(nums)):
            ans[i] *= pre
            ans[-1-i] *= post
            pre, post = pre*nums[i], post*nums[-1-i]
        return ans
