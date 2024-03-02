'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        check = {}
        ans =[]
        for i in nums:
            if i in check:
                if(check[i]!=-1):
                    check[i] = check[i]+1
            else:
                check[i] = 1
            
            if(check[i]>len(nums)/3 and check[i]!=-1):
                ans.append(i)
                check[i]=-1
        

        return ans





'''
for i in nums:
            if i in check:
                check[i] = check[i]+1
            else:
                check[i] = 1
        
        for keys in check:
            if(check[keys]>len(nums)/3):
                ans.append(keys)
        

        return ans
'''