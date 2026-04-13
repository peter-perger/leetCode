"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.
Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. 
After removing duplicates, return the number of unique elements k.
The first k elements of nums should contain the unique numbers in sorted order. 
The remaining elements beyond index k - 1 can be ignored.
"""


class Solution(object):
    def removeDuplicates1(self, nums):
        if not nums:
            return 0
        
        j = 0

        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]

        return j + 1
    
    def removeDuplicates2(self, nums):
        if not nums:
            return 0
        
        j = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                j += 1
                nums[j] = nums[i]
                
        return j + 1
            

        

        
nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1,1,2]


solution = Solution()
print(solution.removeDuplicates1(nums))
print(solution.removeDuplicates2(nums))
