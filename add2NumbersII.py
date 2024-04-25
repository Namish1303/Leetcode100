# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        one = 0
        two = 0
        while(l1!=None or l2!=None):
            if(l1!=None):
               one+=1 
               l1=l1.next
            if(l2!=None):
                two+=1
                l2=l2.next
        
        