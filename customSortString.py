'''
You are given two strings order and s. 
All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. 
More specifically, if a character x occurs before a character y in order, 
then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

'''
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order=[x for x in order]
        s= [y for y in s]
        ans=""
        dic = {}
        for i in range(len(order)):
            if(order[i] in s):
                x=0
                while(x!=len(s)):
                    if s[x]==order[i]:
                        ans+=s[x]
                        s.pop(x)
                        continue
                    x+=1
            else:
                continue
        s.sort()
        for i in s:
            ans+=i
    
        return ans
            