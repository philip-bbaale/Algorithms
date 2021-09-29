class Solution:
    def romanToInt(self, s):
        
        romans = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, }
        count = romans[s[-1]]

        for i in range(len(s)-2,-1,-1):
            if romans[s[i]] < romans[s[i+1]]:
                count -= romans[s[i]]
            else:
                count += romans[s[i]]
        
        return count