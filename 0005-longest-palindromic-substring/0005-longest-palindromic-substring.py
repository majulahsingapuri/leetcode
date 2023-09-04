class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        longLen = 0

        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if longLen < r - l + 1:
                    longLen = r - l + 1
                    longest = s[l: r + 1]
                l -= 1
                r += 1
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if longLen < r - l + 1:
                    longLen = r - l + 1
                    longest = s[l: r + 1]
                l -= 1
                r += 1
        return longest
        