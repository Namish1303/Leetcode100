'''
Given an integer array nums, move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x=0
        for i in nums:
            if i!=0:
                x+=1
        i=0
        while(i<x):
            if(nums[i]==0):
                nums.pop(i)
                nums.append(0)
            else:
                i+=1
        
