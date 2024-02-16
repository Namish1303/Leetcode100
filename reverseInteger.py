'''Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
 then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).'''

class Solution:
    def reverse(self, x: int) -> int:
        output = 0
        minus= False
        while(x!=0):
            last = abs(x)%10
            if(x<0):
                minus= True
            
            output = (output*10)+last
            x = int(x/10)
            if(abs(output)<2**31 and output != (2**31)-1):
                continue
            else:
                return 0
    
        if(minus):
            return 0-output
            
        return output
            
            
            