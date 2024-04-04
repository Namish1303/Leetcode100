'''
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
 An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.
'''
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True

        for i in range(0,len(nums)-1) :
            if(nums[i]>nums[i+1] and increasing):
                increasing = False
            if(nums[i]<nums[i+1] and decreasing):
                decreasing = False

            
            if(not increasing and not decreasing):
                return False
        return True