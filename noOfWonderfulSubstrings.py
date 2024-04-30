'''
A wonderful string is a string where at most one letter appears an odd number of times.

For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), 
return the number of wonderful non-empty substrings in word. 
If the same substring appears multiple times in word, then count each occurrence separately.

A substring is a contiguous sequence of characters in a string.
'''
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        num = len(word)
        for i in range(len(word)-1):
            check = word[i]
            singles = []
            singles.append(word[i])
            
            for j in range(i+1,len(word)):
                check+=word[j]
                if(word[j] in singles):
                    singles.remove(word[j])
                else:
                    singles.append(word[j])
                
                if(len(singles)<=1):
                    num+=1
    
        return num