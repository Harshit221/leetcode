from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        carry = (l1.val+l2.val)//10
        res = ListNode((carry + l1.val + l2.val)%10)
        head = res
        l1 = l1.next
        l2 = l2.next
        while l1.next and l2.next:
            res.next = ListNode((carry + l1.val + l2.val)%10)
            carry = (l1.val+l2.val)//10
            l1 = l1.next
            l2 = l2.next
            
        while l1.next:
            res.next = ListNode((carry+l1.val)%10)
            carry = (carry+l1.val)//10
            l1 = l1.next
        while l2.next:
            res.next = ListNode((carry+l2.val)%10)
            carry = (carry+l2.val)//10
            l2 = l2.next
        
        if carry>0:
            res.next = ListNode(carry)
            
        return head
    

