'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        arri=[]
        arrj=[]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j]==0):
                    arri.append(i)
                    arrj.append(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(i in arri or j in arrj):
                    matrix[i][j]=0
