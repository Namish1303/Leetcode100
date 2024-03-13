'''
Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, 
return -1. It is guaranteed that there will be at most one pivot index for the given input.
'''
class Solution:
    def pivotInteger(self, n: int) -> int:
        pivot = True
        if(n==1):
            return 1
        start = 2
        end = n
        ans1=0
        ans2=0

        for x in range(int(n/2)+2):
            ans1+=x
        
        for x in range(int(n/2)+1,n+1):
            ans2+=x
        
        for i in range(int(n/2)+1,n):
            if(ans1 == ans2):
                return i
            else:
                ans1+=i+1
                ans2-=i
                print(ans1,ans2)
        

        return -1
    


        
        return -1