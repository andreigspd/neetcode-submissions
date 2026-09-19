# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        dummy = ListNode()
        curr = dummy
        q = []
        for idx, list in enumerate(lists):
            if list:
                heapq.heappush(q, (list.val, idx, list))
                list = list.next
        while q:
            val, idx, list = heapq.heappop(q)
            curr.next = list
            list = list.next
            curr = curr.next
            if list:
                heapq.heappush(q, (list.val, idx, list))
        return dummy.next
