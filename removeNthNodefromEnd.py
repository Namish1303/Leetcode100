'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        check = head
        l=-1
        while(check!=None):
            l+=1
            check=check.next

        if(l-n+1<=0):
            return head.next
        c=0
        check = head
        while(c<=l):
            if(c==l-n):
                if(head.next!=None):
                    temp = head.next
                    temp = temp.next
                    head.next = temp
                else:
                    head.next = None
                break
            head=head.next
            c+=1
        

        return check