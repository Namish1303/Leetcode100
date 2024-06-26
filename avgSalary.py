'''
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. 
Answers within 10-5 of the actual answer will be accepted.
'''
class Solution:
    def average(self, salary: List[int]) -> float:
        low = salary[0]
        high = salary[0]
        s =0
        for i in salary:
            if i <= low:
                low = i
            
            if i>high:
                high = i
            
            s+=i

        s= s -low -high
        s = s/(len(salary)-2)

        return s
        
