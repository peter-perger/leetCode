"""
Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.
"""

class Solution(object):
    def findDissapearedNumbers(self, nums):
        set_nums = set(nums)
        result = []

        for i in range(1, len(nums) + 1):
            if i not in set_nums:
                result.append(i)

        return result
        
nums = [4,3,2,7,8,2,3,1]
nums2 = [1,1]
nums3 = [1, 2]

len(nums2)   # >> 2
range(2)     # >> range(0, 1)





solution = Solution()
print(solution.findDissapearedNumbers(nums))
print(solution.findDissapearedNumbers(nums2))
print(solution.findDissapearedNumbers(nums3))

