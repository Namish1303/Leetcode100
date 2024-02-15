'''You are given two non-empty linked lists representing two non-negative integers.
 The digits are stored in reverse order, and each of their nodes contains a single digit. 
 Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l_l1 =1
        l_l2 =1

        n_l1=l1
        n_l2=l2
        for i in range(101):
            if(n_l1.next!=None):
                n_l1= n_l1.next
                l_l1+=1
            
            if(n_l2.next!=None):
                n_l2 = n_l2.next
                l_l2+=1
        
            if(l1.next == None and l2.next==None):
                break
        
        if(l_l1 >=l_l2):
            head = l1
            head2 = l2
        else:
            head = l2
            head2= l1

        add1 = False
        while(head !=None):
            if(head2 != None):
                value = head.val+head2.val
                if(add1):
                    value +=1
                    add1 = False
                if(value >=10):
                    value = value%10
                    add1=True
                head.val = value
                if(head.next==None and add1):
                    head.next=ListNode(0)
                head = head.next
                head2 = head2.next
            else:
                value = head.val
                if(add1):
                    value +=1
                    add1 = False
                if(value >=10):
                    value = value%10
                    add1=True
                head.val = value
                print(head.val)
                if(head.next==None and add1):
                    head.next=ListNode(0)
                head = head.next               
        
        if(l_l1>=l_l2):
            return l1
        else:
            return l2


