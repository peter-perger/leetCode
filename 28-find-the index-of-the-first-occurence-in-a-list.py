class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            word = haystack[i:i+len(needle)]
            
            if word == needle:
                return i

        return -1

haystack = "estoptup"
needle = "tup"

solution = Solution()
print(solution.strStr(haystack, needle))
