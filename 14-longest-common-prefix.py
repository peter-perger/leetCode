"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        prefix = strs[0]

        for string in strs[1:]:
            while string.find(prefix) != 0:
                prefix = prefix[:-1]

                if not prefix:
                    return ""
        
        return prefix



strs0 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]
strs3 = ["a"]
strs4 = ["ab", "a"]

solution = Solution()
print(solution.longestCommonPrefix(strs0))
# print(solution.longestCommonPrefix(strs2))
# print(solution.longestCommonPrefix(strs3))
print(solution.longestCommonPrefix(strs4))