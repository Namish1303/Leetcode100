'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=[]
        even = True
        while(len(nums1)>0 or len(nums2)>0):
            if(len(nums1)<=0):
                arr.append(nums2[0])
                nums2.pop(0)
            elif(len(nums2)<=0):
                arr.append(nums1[0])
                nums1.pop(0)
            else:
                if(nums1[0]<nums2[0]):
                    arr.append(nums1[0])
                    nums1.pop(0)
                else:
                    arr.append(nums2[0])
                    nums2.pop(0)
            even = not even
        
        if(even):
            return ((arr[int(len(arr)/2)-1])+(arr[int(len(arr)/2)]))/2
        else:
            return (arr[len(arr)//2])