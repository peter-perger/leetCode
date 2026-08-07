"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

class Solution:
    def longestCommonPrefix(self, strs):
        if not str:
            return ""

        prefix = strs[0]

        for word in strs:
            if word.find(prefix) != 0:
                prefix = prefix[:-1]

                if not prefix:
                    return ""

        return prefix

            

words = [
    "precaution",
    "precede",
    "precise",
    "preclude",
    "predict",
    "preface",
    "prefer",
    "prefix",
    "prehistoric",
    "prejudge",
    "prelude",
    "premise",
    "premium",
    "prepare",
    "preposition",
    "preschool",
    "prescribe",
    "present",
    "preserve",
    "presume",
]

solution = Solution()
print(solution.longestCommonPrefix(words))
