class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        letters = set(s)
        for letter in letters:
            counts[letter] = 0
        for letter in s:
            counts[letter] += 1
        pivot = False
        result = 0
        print(counts)
        for count in counts.values():
            print("count: ", count)
            if count == 1:
                if not pivot:
                    pivot = True
                else:
                    count = 0
            elif count % 2 != 0:
                if not pivot:
                    pivot = True
                else:
                    count -= 1
            result += count
            print("result: ",result)
                
        return result
