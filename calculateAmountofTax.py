'''You are given a 0-indexed 2D integer array brackets where 
brackets[i] = [upperi, percenti] means that the ith tax bracket has an upper bound of upperi 
and is taxed at a rate of percenti. 
The brackets are sorted by upper bound (i.e. upperi-1 < upperi for 0 < i < brackets.length).
'''

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        if(brackets[0][0]>= income):
            tax += income * brackets[0][1] / 100
            return tax
        else:
            tax += brackets[0][0] * brackets[0][1]/100
            income -= brackets[0][0]


        for i in range(1,len(brackets)):
            b = brackets[i]
            gap = b[0] - brackets[i-1][0]
            if(gap>=income):
                tax += income * b[1] / 100
                income= 0
                break
                
            else:
                tax += gap * b[1] /100
                income -= gap

        return tax
