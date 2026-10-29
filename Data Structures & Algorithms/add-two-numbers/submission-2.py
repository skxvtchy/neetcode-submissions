# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        one=""
        two=""
        res = ListNode()
        resi = res


        while l1.next!=None:
            one+=(str(l1.val))
            l1=l1.next
        one+=(str(l1.val))
        l1=l1.next  
        while l2.next!=None:
            two+=(str(l2.val))
            l2=l2.next
        two+=(str(l2.val))
        l2=l2.next

        yea = (int(one[::-1])+int(two[::-1]))

        for i in str(yea)[::-1]:
            res.next = ListNode(i)
            res=res.next
        return resi.next
  