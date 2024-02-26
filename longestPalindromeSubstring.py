'''
Given a string s, return the longest palindromic substring in s.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checkPalindrome(s):
            for i in range(int(len(s)/2)):
                if(s[i] != s[len(s)-1-i]):
                    return False
            return True
        
        i=0
        j=len(s)
        if(checkPalindrome(s)):
            return s
        while(j>=len(s)/2):
            if(checkPalindrome(s[i:])):
                print("i:  ",s[i:])
                return s[i:]
            if(checkPalindrome(s[:j])):
                print("j:  ",s[:j])
                return s[:j]
            if(checkPalindrome(s[i:j])):
                print("i: ",i)
                print("j: ",j)
                print("i and j:  ",s[i:j])
                return s[i:j]
            i+=1
            j-=1
        
        return ""
