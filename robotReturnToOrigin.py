'''
There is a robot starting at the position (0, 0), the origin, on a 2D plane. 
Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

You are given a string moves that represents the move sequence of the robot where 
moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

Note: The way that the robot is "facing" is irrelevant. 
'R' will always make the robot move to the right once, 
'L' will always make it move left, etc. 
Also, assume that the magnitude of the robot's movement is the same for each move.

 

'''
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        h=0
        v=0

        for i in moves:
            if(i=='L'):
                h+=1
            elif(i=='R'):
                h-=1
            elif(i=='D'):
                v-=1
            else:
                v+=1
        
        if(h==0 and v==0):
            return True
        
        return False

'''
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('L')==moves.count('R') and moves.count('U')==moves.count('D')

'''