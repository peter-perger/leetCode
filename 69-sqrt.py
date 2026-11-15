"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python
"""

class Solution():
    def sqrt(self, x):
        low = 0
        high = x
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            midsq = mid * mid

            if midsq == x:
                return mid

            elif midsq > x:
                high = mid -1

            else:
                ans = mid
                low = mid + 1
        
        return ans


if __name__ == '__main__':
    num = 84;
    
    sol = Solution()
    print(sol.sqrt(num))
            