class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        counter = Counter(nums)
        perm = []

        def dfs():
            if len(perm) == len(nums):
                result.append(perm.copy())

            for n in counter:
                if counter[n] > 0:
                    perm.append(n)
                    counter[n] -= 1
                    dfs()
                    perm.pop()
                    counter[n] += 1

        dfs()

        return result
