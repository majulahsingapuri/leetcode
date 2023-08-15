class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            sala={}
            nala={}
            for i in s:
                if i in sala:
                    sala[i] += 1
                else:
                    sala[i] = 1
            for i in t:
                if i in nala:
                    nala[i] += 1
                else:
                    nala[i] = 1
            return sala == nala
