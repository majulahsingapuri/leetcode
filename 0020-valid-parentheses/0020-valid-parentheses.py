class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }

        for char in s:
            if char == '[' or char == '{' or char == '(':
                stack.append(char)
            else:
                try:
                    val = stack.pop()
                except:
                    val = None
                if not val or val != pairs[char]:
                    return False
                        
        return True if len(stack) == 0 else False