'''
You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x = ""
        i=0
        j=0
        while(len(x) != len(word1)+len(word2)):
            if(i!=-1):
                print(i)
                x+=word1[i]
                i+=1
            if(j!=-1):
                print("j:  ",j)
                #print(word2[j])
                x+=word2[j]
                j+=1
            
            if(i>len(word1)-1):
                i=-1
            if(j>len(word2)-1):
                j=-1
                
        return x