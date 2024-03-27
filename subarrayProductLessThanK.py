'''

Given an array of integers nums and an integer k, return the number of contiguous subarrays 
where the product of all the elements in the subarray is strictly less than k.
'''
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if(k<=1):
            return 0
            
        product = 1
        count = 0
        left = 0

        for right, num in enumerate(nums):
            product *= num
            while product >= k:
                print(left)
                product /= nums[left]
                left += 1
            count += right-left+1
        
        return count
