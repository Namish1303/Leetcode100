'''
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if(head.next==None):
            return True
        check = head
        l=0
        while(check!= None):
            l +=1
            check=check.next

        i=1
        check = []
        while(head!=None):
            if(i<=l//2):
                print("here")
                check.append(head.val)

            elif(l%2 !=0 and i==(l//2)+1):
                x=None
            else:
                if(head.val == check[-1]):
                    print("hey")
                    check.pop(-1)
                else:
                    return False
            head=head.next
            i+=1

        return True