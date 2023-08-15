class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        cur = head
        old_next = cur.next
        new_next = None
        
        while (cur):
            cur.next = new_next
            new_next = cur
            cur = old_next
            if cur:
                old_next = cur.next
        
        return new_next