# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        q = []
        for idx, list in enumerate(lists):
            if list:
                heapq.heappush(q, (list.val, idx, list))
        dummy = ListNode()
        head = dummy
        while q:
            _, idx, node = heapq.heappop(q)
            head.next = node
            head = head.next
            node = node.next
            if node:
                heapq.heappush(q, (node.val, idx, node))
        return dummy.next