'''
There are some spherical balloons taped onto a flat wall that represents the XY-plane. 
The balloons are represented as a 2D integer array points
 where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches 
 between xstart and xend. 
 You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points 
along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. 
There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, 
bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

'''

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x:x[1])
        arrows=0
        end = None
        for i in points:
            if(end is None or end <i[0]):
                end = i[1]
                arrows+=1
        


        return arrows

'''
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows=0

        while(len(points)>0):
            #print(points)
            start = points[len(points)-1][0]
            x=len(points)-2
            while(x>=0):
                if(start <= points[x][1] and start>= points[x][0]):
                   # print("arrow:  ",arrows,"     points:    ",points[x])
                    points.pop(x)
                    x-=1
                else:
                    x-=1
            points.pop(len(points)-1)
            arrows+=1    


        return arrows



'''