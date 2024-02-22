'''Given an integer array nums, 
move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.'''

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if(len(nums)==0):
            return nums
        
        sort=[0]*len(nums)
        j=0
        x=len(nums)-1
        for i in nums:
            if(i%2==0):
                sort[j]=i
                j+=1
            else:
                sort[x] = i
                x-=1
        




        return sort 