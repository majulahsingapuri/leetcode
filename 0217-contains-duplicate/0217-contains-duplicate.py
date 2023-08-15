class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for curr in nums:
            if curr in seen:
                return True
            else:
                seen.add(curr)
        return False
