"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
"""

class Solution():
    def lengthOfLastWord(self, s):
            words = s.split(" ")

            for word in words[::-1]:
                  if word != "":
                        return len(word)



s = "Hello World"
s1 = "   fly me   to   the moon  "
s2 = "luffy is still joyboy"

solution = Solution()
print(solution.lengthOfLastWord(s))
print(solution.lengthOfLastWord(s1))
print(solution.lengthOfLastWord(s2))