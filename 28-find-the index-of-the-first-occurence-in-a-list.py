"""Given two strings needle and haystack
   return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack."""


class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.find(needle)
        

haystack = "estoptup"
needle = "tup"

haystack2 = "vvvvvv"
needle2 = 'iiii'

solution = Solution()
print(solution.strStr(haystack, needle))
print(solution.strStr(haystack2, needle2))
