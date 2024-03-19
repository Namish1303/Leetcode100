'''
Determine if a 9 x 9 Sudoku board is valid. 
Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            check = []
            for x in range(len(board[i])):
                if(board[i][x] in check and board[i][x] is not "."):
                    return False
                else:
                    check.append(board[i][x])

        
        for i in range(9):
            check = []
            for x in range(9):
                if(board[x][i] in check and board[x][i] is not "."):
                    return False
                else:
                    check.append(board[x][i])

        for a in range(3):
            for b in range(3):
                check = []
                for i in range(3*a,3*a+3):
                    for j in range(3*b,3*b+3):
                        if(board[i][j] in check and board[i][j] is not "."):
                            return False
                        else:
                            check.append(board[i][j])
        return True
        

