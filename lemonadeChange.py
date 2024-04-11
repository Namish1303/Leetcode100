'''
At a lemonade stand, each lemonade costs $5. 
Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). 
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. 
You must provide the correct change to each customer so that the net transaction is that the customer pays $5.


Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, 
return true if you can provide every customer with the correct change, or false otherwise.
'''

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        notes = {5:0,10:0,20:0}

        for i in bills:
            #print(notes)
            if(i == 5):
                notes[5]+=1
            
            elif(i==10):
                if(notes[5]>=1):
                    notes[5]-=1
                    notes[10]+=1
                else:
                    return False
            
            else:
                if(notes[10]>=1 and notes[5]>=1):
                    notes[10]-=1
                    notes[5]-=1
                    notes[20]+=1
                elif(notes[5]>=3):
                    notes[5]-=3
                    notes[20]+=1
                else:
                    return False
            

        return True