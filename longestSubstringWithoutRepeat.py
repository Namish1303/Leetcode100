'''
Given a string s, find the length of the longest substring without repeating characters.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checked ={}
        length =0
        answer = 0

        for i in range(len(s)):
            if s[i] not in checked:
                answer = max(answer,i-length+1)
            
            else:
                if(checked[s[i]] < length):
                    answer = max(answer,i-length+1)
                else:
                    length = checked[s[i]]+1
            
            checked[s[i]]=i
        
        return answer
