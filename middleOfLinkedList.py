'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        middle = head
        head=head.next

        while(head!=None):
            length +=1
            if(length%2==0):
                middle=middle.next
                head=head.next
            else:
                head = head.next
        

        return middle