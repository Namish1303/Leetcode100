'''
A sequence of numbers is called an arithmetic progression 
if the difference between any two consecutive elements is the same.

Given an array of numbers arr, 
return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.
'''
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        x = arr[1] - arr[0]

        for i in range(1,len(arr)-1):
            check = arr[i+1] - arr[i]

            if(check != x):
                return False
        

        return True