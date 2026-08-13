"""
Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        seen = []

        for num in nums:
            if num in seen:
                return True
            
            seen.append(num)

        return False

    def containsDuplicate2(self, nums):
        return len(nums) != len(set(nums))

    def containsDuplicate3(self, nums):
        for i in range(len(nums) - 1):

            for j in range(i + 1, len(nums)):
                if nums[j] == nums[i]:
                    return True

        return False


input_nums = [1, 2, 3, 1]
input_nums2 = [1, 2, 5, 3]

solution = Solution()
print(solution.containsDuplicate3(input_nums))
print(solution.containsDuplicate3(input_nums2))

