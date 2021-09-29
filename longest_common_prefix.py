class Solution:
    def longestCommonPrefix(self, strs):
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

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""