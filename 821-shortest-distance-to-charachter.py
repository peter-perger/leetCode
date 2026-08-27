"""
Given a string s and a character c that occurs in s, 
return an array of integers answer where answer.length == s.length and answer[i] 
is the distance from index i to the closest occurrence of character c in s.

The distance between two indices i and j is abs(i - j), where abs is the absolute value function.
"""

class Solution():
    def shortestToChar(self, s, c): #c"aaababaaba" || "c"
        n = len(s)  # 10
        temp = []   # [3, 5, 8]
        result = []
        
        for i in range(n):
            if(s[i] == c):
                temp.append(i)
        
        m = len(temp) # 3
        
        j = 0

        for i in range(n):
            dist = abs(temp[j] - i)
            while(j < m - 1 and abs(temp[j + 1] - i) <= dist):
                j += 1
                dist = abs(temp[j] - i)
            
            result.append(dist)
        
        return result
        
        
if __name__ == '__main__':
    solution = Solution()

    s = "aaababbb"
    c = "b"

    print(solution.shortestToChar(s, c))

    

