class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for curr in strs:
            temp = str(sorted(curr))
            if temp in dic:
                dic[temp].append(curr)
            else:
                dic[temp] = [curr]
        return list(dic.values())
            
        