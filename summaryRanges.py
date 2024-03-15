'''
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, 
and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
'''

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        end =0
        ans=[]
        while(end!=len(nums)):
            if(end == len(nums)-1):
                if(end ==0):
                    ans.append(str(nums[end]))
                    break
                else:
                    ans.append(str(nums[0])+"->"+str(nums[end]))
                    break
            else:
                if(nums[end]==nums[end+1]-1):
                    #print(nums[end],nums[end+1])
                    end+=1
                else:
                    if(end ==0):
                        ans.append(str(nums[end]))
                        nums.pop(0)
                        
                    else:
                        ans.append(str(nums[0])+"->"+str(nums[end]))
                        nums=nums[end+1:]
                        end=0
        
        return ans