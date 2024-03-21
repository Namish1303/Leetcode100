'''

Given the head of a singly linked list, reverse the list, and return the reversed list.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None or head.next==None):
            return head 
        prev = head
        check = head.next
        nex = None
        while(check!= None):
            
            nex = check.next
            #print(nex.val,check.val,prev.val)
            check.next = prev
            prev = check
            check = nex
        head.next = None
        return prev

        
    