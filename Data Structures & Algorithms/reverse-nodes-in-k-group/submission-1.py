# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        dummy = ListNode(0, head)
        i = 0
        prev_head = dummy
        new_head = None
        new_tail = None
        curr = head
        prev = None
        while i + k <= n:
            right = k - 1
            new_tail = curr
            while right > -1:
                urm = curr.next
                curr.next = prev
                prev = curr
                curr = urm
                right -= 1
            new_head = prev
            prev_head.next = new_head
            new_tail.next = curr
            prev_head = new_tail
            i += k
        return dummy.next
