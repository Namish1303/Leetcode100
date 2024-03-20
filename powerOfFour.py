'''
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

'''

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i=0
        while(1==1):
            if(4**i > n):
                return False
            elif(4**i == n):
                return True
            else:
                i+=1
        return False