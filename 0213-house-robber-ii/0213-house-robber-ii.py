class Solution:
    def _rob(self, nums:List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        elif size == 1:
            return nums[0]
        elif size == 2:
            return max(nums)
        for i in range(size - 3, -1, -1):
            jump_2 = nums[i + 2] if i + 2 < size else 0
            jump_3 = nums[i + 3] if i + 3 < size else 0
            nums[i] += max(jump_2, jump_3)
            
        return max(nums[0], nums[1])

    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        elif size == 1:
            return nums[0]
        elif size == 2:
            return max(nums)
        return max(self._rob(nums[:-1]), self._rob(nums[1:]))