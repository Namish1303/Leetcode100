'''You are given an array of positive integers nums of length n.

A polygon is a closed plane figure that has at least 3 sides. 
The longest side of a polygon is smaller than the sum of its other sides.

Conversely, if you have k (k >= 3) positive real numbers a1, a2, a3, ..., ak where a1 <= a2 <= a3 <= ... <= ak and a1 + a2 + a3 + ... + ak-1 > ak, 
then there always exists a polygon with k sides whose lengths are a1, a2, a3, ..., ak.

The perimeter of a polygon is the sum of lengths of its sides.

Return the largest possible perimeter of a polygon whose sides can be formed from nums, or -1 if it is not possible to create a polygon.

 '''

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if(len(nums)<=2):
            return -1
        nums.sort(reverse=True)
        if(len(nums) ==3):
            if(nums[0] >= nums[1]+nums[2]):
                return -1
            else:
                return nums[0]+nums[1]+nums[2]

        found = False
        answer=0
        while(not found):
            if(len(nums)<=2):
                return -1
            total =0
            for j in range(1,len(nums)):
                total += nums[j]
                
                if(total > nums[0]):
                    found = True
                    break
            if(not found):
                nums.pop(0)
                
            else:
                break
        x=0
        for i in nums:
            x+=i
            
        return x