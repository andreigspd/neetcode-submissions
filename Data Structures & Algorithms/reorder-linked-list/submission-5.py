# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        prev_half = None
        curr = slow
        while curr:
            urm = curr.next
            curr.next = prev_half
            prev_half = curr
            curr = urm
        

        curr = prev_half
        start = head
        while curr:
            urm_start = start.next
            urm_half = curr.next
            start.next = curr
            if urm_start is None:
                break
            curr.next = urm_start
            curr = urm_half
            start = urm_start
        
            