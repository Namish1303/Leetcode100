'''
Given an integer array nums of length n where all the integers of nums are in the range 
[1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mid = 0 
        dic = {}
        num2=[]
        for i in nums:
            if i in dic:
                num2.append(i)
            else:
                dic[i] = 1
        
        return num2