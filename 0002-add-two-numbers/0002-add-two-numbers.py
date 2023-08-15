# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = None
        cur = None
        while (l1 or l2):
            _sum = carry
            if l1:
                _sum += l1.val
            if l2:
                _sum += l2.val
            carry = _sum // 10
            val = _sum % 10
            node = ListNode(val)
            if result:
                cur.next = node
                cur = cur.next
            else:
                result = node
                cur = node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if (carry):
            node = ListNode(carry)
            cur.next = node


        return result


            