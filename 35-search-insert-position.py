"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        
        i = 0

        while i < len(nums) - 1:
            next_num = nums[i + 1]

            if target > nums[i] and target < next_num:
                return i + 1
            
            i += 1
        
        if target < nums[0]:
            return 0
        
        return len(nums)

nums0 = [1,3,5,6]
target0 = 5

nums1 = [1,3,5,6] 
target1 = 2

nums2 = [1,3,5,6] 
target2 = 7

solution = Solution()
print(solution.searchInsert(nums=nums0, target=target0))
print(solution.searchInsert(nums1, target1))
print(solution.searchInsert(nums2, target2))
        

