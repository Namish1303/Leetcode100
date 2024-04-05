'''
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
'''
class Solution:
    def toLowerCase(self, s: str) -> str:
        ans=""
        for i in s:
            if(ord(i)>=65 and ord(i)<=90):
                ans += chr(ord(i)+32)
            else:
                ans+=i
        return ans

'''class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()'''