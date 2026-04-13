"Given an integer x, return true if x is a palindrome, and false otherwise."

class Solution:
    def isPalindrome(self, x):
        num_str = str(x)
        #This is called String Slicing. The syntax for a slice is [start:stop:step]
        return num_str == num_str[::-1]
    
    def isPalindrome2(self, x):
        if x < 0:
            return False
        
        rev = 0 
        num = x

        while num != 0:
            rev = rev * 10 + num % 10
            num = num // 10

        return rev == x
    

num = 143341
num2 = 1232544

solution = Solution()
print(solution.isPalindrome(num))
print(solution.isPalindrome2(num2))
        