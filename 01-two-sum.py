"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order. 
"""

nums = [1, 5, 6, 2, 4, 3]
target = 8

class Solution:
    def two_sum(self, nums, target):
        num_map = {}

        for i, num in enumerate(nums):
            complementer = target - num

            if complementer in num_map:
                return [num_map[complementer], i]

            num_map[num] = i  

        return []      


solution = Solution()
result = solution.two_sum(nums, target)
print(result)
