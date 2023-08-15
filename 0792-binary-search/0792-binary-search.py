class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        # Get the left middle and right pointers
        left, right = 0, len(nums) - 1

        def binSearch(left, right):
            if right <= left:
                if nums[left] == target:
                    return left
                else:
                    return -1
            else:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    return binSearch(left, mid - 1)
                else:
                    return binSearch(mid + 1, right)

        return binSearch(left, right)