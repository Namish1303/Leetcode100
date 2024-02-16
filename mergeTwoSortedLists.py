'''You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. 
The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1 == None):
            return list2
        elif(list2 == None):
            return list1
        l1 = 1
        l2 = 1
        n1 = list1
        n2 = list2
        for i in range(51):
            if(n1.next!=None):
                n1=n1.next
                l1+=1
            if(n2.next!=None):
                n2=n2.next
                l2+=1
            if(n1.next==None and n2.next==None):
                break
        
        l = 1
        if(list1.val <= list2.val):
            h = list1
            list1=list1.next
        else:
            h = list2
            list2=list2.next
        n = h
        while(l!=l1+l2):
            if(list1==None and list2==None):
                break
            elif(list1==None):
                h.next = list2
                h = h.next
                list2=list2.next
            elif(list2==None):
                h.next = list1
                h= h.next
                list1 = list1.next
            else:
                if(list1.val <= list2.val):
                    h.next = list1
                    h = h.next
                    list1 = list1.next
                else:
                    h.next = list2
                    h=h.next
                    list2 = list2.next
            l+=1

        return n