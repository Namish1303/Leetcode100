'''Given two integers num and k, consider a set of positive integers with the following properties:

The units digit of each integer is k.
The sum of the integers is num.
Return the minimum possible size of such a set, or -1 if no such set exists.

'''
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if(num==0):
            return 0
        if((k==0 and num%10!=0) or k>num):
            return -1
        
        digits =0
        for i in range(1,11):
            if((num - (k*i))%10 == 0):
                if((k*i)>num):
                    break
                return i
            
        return -1