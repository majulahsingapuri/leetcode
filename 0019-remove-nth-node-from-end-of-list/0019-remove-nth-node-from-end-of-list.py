# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        memo = {}
        count = 1

        cur = head
        while cur:
            memo[count] = cur
            cur = cur.next
            count += 1
        
        prev = memo.get(count - n - 1)
        target = memo[count - n]
        after = memo.get(count - n + 1)

        target.next = None
        if prev:
            prev.next = after
        else:
            head = after

        return head
