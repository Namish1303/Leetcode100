'''
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
return the minimum integer common to both arrays. 
If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays 
have at least one occurrence of that integer.
'''
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        found = False 
        i1 = 0
        i2 =0
        if(nums1[len(nums1)-1] < nums2[0]):
            return -1
        while(not found):
            if((i2 > len(nums2)-1 or i1>len(nums1)-1) and not found):
                return -1
            if(nums1[i1] == nums2[i2]):
                return nums1[i1]
            elif(nums1[i1]<nums2[i2]):
                i1+=1
            else:
                i2+=1

            
            
            
        
        return -1
