class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        
        def search(cur):
            if cur > target:
                return
            if cur == target:
                new_path = path.copy()
                new_path.sort()
                if new_path not in res:
                    res.append(new_path)
                return
            for candidate in candidates:
                path.append(candidate)
                search(cur + candidate)
                path.pop(-1)

        search(0)
        return res
            