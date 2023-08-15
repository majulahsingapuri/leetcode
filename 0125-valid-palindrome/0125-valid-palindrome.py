import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^a-zA-Z0-9]", "", s)
        s = s.lower()
        len_s = len(s)
        print(s)
        for i in range(len_s // 2):
            if s[i] != s[len_s - i - 1]:
                return False
        return True