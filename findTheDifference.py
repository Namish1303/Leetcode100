'''
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.

'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}
        for i in s:
            if(i in d):
                d[i]+=1
            else:
                d[i] = 1
        
        d2 = {}
        for i in t:
            if(i not in d2):
                d2[i]=1
                if(i not in d):
                    return i
            else:
                d2[i]+=1
                if(d2[i] == d[i]+1):
                    return i
        
        return "cd"

'''


'''