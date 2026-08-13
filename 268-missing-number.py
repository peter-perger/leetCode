"""
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
"""

class Solution(object):
    def missingNumber(self, nums):
        nums = sorted(nums)

        for i, num in enumerate(nums):
            if i != num:
                return i


        return nums[-1] + 1

    def missingNumber2(self, nums):
        return sum(range(len(nums) + 1)) - sum(nums)

            

nums = [0, 1, 4, 2]

# print(sum(list(range(len(nums)))))
# print(sum(list(range(len(nums) + 1))))

solution = Solution()
#print(solution.missingNumber(nums))
#print(solution.missingNumber2(nums))
#print(solution.missingNumber(nums))

sum(nums)       # >> 0 + 1 + 2 + 4 = 7

len(nums)       # >> 4
len(nums) + 1   # >> 5
range(5)        # >> range(0, 4)
sum(range(5))   # >> 0 + 1 + 2 + 3 + 4 = 10 

