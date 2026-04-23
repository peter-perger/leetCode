"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution():
    def validParentheses(self, s):
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []


        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or mapping[char] != stack.pop():
                    return False

        return not stack


        
        

solution = Solution()
print(solution.validParentheses("()"))
# print(solution.validParentheses("([]{})"))
# print(solution.validParentheses("([)])"))
