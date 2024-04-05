'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        check = 0
        for i in range(len(s)-1,-1,-1):
            if(check == 0 and s[i]==" "):
                continue
            elif(check!= 0 and s[i] == " "):
                break
            else:
                check+=1
        

        return check