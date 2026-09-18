# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        from collections import defaultdict
        freq = defaultdict(ListNode)
        curr = head
        while curr:
            if curr in freq:
                return True
            freq[curr] = 1
            curr = curr.next
        return False