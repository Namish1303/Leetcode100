'''
You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:



'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        end = list2
        while(end.next != None):
            end = end.next

        
        start = 0
        temps = None
        tempe = None
        check = list1
        while(1==1):
            if(start == a-1):
                temps = check
            if(start == b):
                tempe = check.next
                break
            start +=1
            check = check.next
        
        temps.next = list2
        end.next = tempe
        return list1