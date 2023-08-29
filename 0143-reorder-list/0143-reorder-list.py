# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        fast = slow = head

        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        prev, cur = None, slow
        while cur:
            next_ = cur.next
            cur.next = prev
            prev = cur
            cur = next_

        left, right = head, prev

        while left and right:
            next_left = left.next
            next_right = right.next
            left.next = right
            right.next = next_left
            left = next_left
            right = next_right
