"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
For example:

A -> 1
B -> 2
C -> 3

Z -> 26
AA -> 27
AB -> 28 
"""

class Solution():
    def convertToTitle(self, columNumber):
        capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        print(capitals)
        result = []

        while columNumber > 0:
            result.append(capitals[(columNumber - 1) % 26])
            columNumber = (columNumber -1) // 26

        result.reverse()
        return ''.join(result)
        
solution = Solution()
print(solution.convertToTitle(2987))