'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
 (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        x = [""]*numRows
        if(numRows==1):
            return s
        z=False
        r=0
        #print(x)
        for i in s:
            if(z):
                x[r]+=i
                r-=1
                if(r<0):
                    z=False
                    r=1

            else:
                x[r]+=i
                r+=1
                if(r==numRows):
                    r=numRows-2
                    z=True

        print(x)
        ans = ""
        for i in x:
            ans+=i
        return ans