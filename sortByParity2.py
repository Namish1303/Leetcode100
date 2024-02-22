'''Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.'''
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = 0
        odd = 1

        while(even<len(nums) and odd<len(nums)):
            if(nums[even]%2 ==0):
                even+=2
            else:
                if(nums[odd]%2!=0):
                    odd+=2
                else:
                    nums[even],nums[odd] = nums[odd],nums[even]
                    even+=2
                    odd+=2


        return nums