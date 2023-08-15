class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        first = letters[0]
        letters = set(letters)
        max_c = max(letters)
        if max_c <= target:
            return first
        for c in letters:
            print(c, target, max_c)
            if target < c < max_c:
                max_c = c
        return max_c
        