"Given an integer x, return true if x is a palindrome, and false otherwise."

class Solution:
    def isPalindrome(self, x):
        num_str = str(x)

        return num_str == num_str[::-1]
    
    def isPalindrome2(self, x):
        num_str = str(x)

        left = 0
        right = len(num_str) - 1

        while left < right:
            if num_str[left] != num_str[right]:
                return False

            left += 1
            right -= 1

        return True

num = 1221
num2 = 12325444452321
num3 = 56876783

solution = Solution()
print(solution.isPalindrome(num2))
print(solution.isPalindrome2(num))
        