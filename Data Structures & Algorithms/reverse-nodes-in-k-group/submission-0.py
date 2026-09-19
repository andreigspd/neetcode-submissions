# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        i = 0
        n = len(arr)
        while i + k <= n:
            left = i
            right = i + k - 1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            i += k
        dummy = ListNode()
        curr = dummy
        for x in arr:
            node = ListNode(x)
            curr.next = node
            curr = curr.next
        return dummy.next

        