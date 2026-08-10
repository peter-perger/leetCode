"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)

        for i in range(len(nums) - 1):
            if nums[0] > target:
                return 0

        if nums[-1] < target:
            return len(nums)
            
        if nums[i] < target and target < nums[i + 1]:
            return i + 1


nums0 = [1,3,5,6]
target0 = 5

nums1 = [2,3,5,6] 
target1 = 1

nums2 = [1,3,5,6] 
target2 = 7

solution = Solution()
#print(solution.searchInsert(nums=nums0, target=target0))
print(solution.searchInsert(nums1, target1))
#print(solution.searchInsert(nums2, target2))
        

