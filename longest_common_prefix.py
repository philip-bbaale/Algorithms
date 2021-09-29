class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        new = list(zip(*strs))
        prefix = ""
        if len(strs) == 0:
            return ""
        if "" in strs:
            return ""
        for item in new:
            if len(set(item)) == 1:
                prefix += item[0]
            else:
                return prefix 
        return prefix