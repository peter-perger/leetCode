"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.
"""

class Solution():
    def smallerNumbersThanCurrent(self, nums):
        result = []
        i = 0

        while i < len(nums):
            count = 0
            current_num = nums[i]

            for num in nums:
                if num < current_num:
                    count += 1

            result.append((count)) 
            i += 1

        return result

    def smallerNumbersThanCurrent2(self, nums):
        temp  = sorted(nums)
        dict = {}

        for i, num in enumerate(temp):
            if num not in dict:
                dict[num] = i

        result = []

        for i in nums:
            result.append(nums[i])

        return result
        
 
nums = [8,1,2,2,3] # 1, 2, 2, 3, 8 >> {1:0, 2:1, 3:3, 8:4}
nums2 = [6,5,4,8]
nums3 = [7,7,7,7]

solution = Solution()
print(solution.smallerNumbersThanCurrent(nums))
print(solution.smallerNumbersThanCurrent(nums2))
print(solution.smallerNumbersThanCurrent(nums3))

print("---------------------")

print(solution.smallerNumbersThanCurrent(nums))
print(solution.smallerNumbersThanCurrent(nums2))
print(solution.smallerNumbersThanCurrent(nums3))