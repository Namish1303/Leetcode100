'''
On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:

"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

'''
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        ar = ["L","U","R","D"]
        di = {"H":0,"V":0}
        direction = 1

        for i in instructions:
            if(i == "L"):
                direction -=1
                if(direction <0):
                    direction = 3
            
            if(i == "R"):
                direction +=1
                if(direction >3):
                    direction = 0
            
            if(i == "G"):
                check = ar[direction]
                if(check == "L"):
                    di["V"]-=1
                elif(check == "R"):
                    di["V"] +=1
                elif(check=="U"):
                    di["H"] +=1
                else:
                    di["H"] -=1
        

        return (di["H"]==0 and di["V"] ==0) or direction!=1
