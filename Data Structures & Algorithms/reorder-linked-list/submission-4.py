# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        curr = slow
        rev_prev = None
        while curr:
            urm = curr.next
            curr.next = rev_prev
            rev_prev = curr
            curr = urm
        first, second = head, rev_prev
        while first and second:
            urm1 = first.next
            urm2 = second.next
            first.next = second
            if urm1 is None:
                break
            second.next = urm1
            first = urm1
            second = urm2