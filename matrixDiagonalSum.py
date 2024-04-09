'''
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal 
and all the elements on the secondary diagonal that are not part of the primary diagonal.
'''
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        si = 0
        ei = 0
        sj = 0
        ej = len(mat)-1

        ans = 0

        while(si!=len(mat)):
            if(si==ei and sj==ej):
                ans += mat[si][sj]
            else:
                ans+= mat[si][sj]
                ans+= mat[ei][ej]
            
            si+=1
            sj+=1
            ei+=1
            ej-=1
        
        return ans
