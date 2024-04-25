'''
Given two binary strings a and b, return their sum as a binary string.
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = int(a,2)+int(b,2)
        c = format(c,'b')
        return c
