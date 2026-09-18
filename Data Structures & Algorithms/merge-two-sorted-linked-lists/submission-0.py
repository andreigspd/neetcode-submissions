# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        curr1, curr2 = list1, list2
        while curr1 or curr2:
            if curr1 and curr2:
                if curr1.val <= curr2.val:
                    node.next = curr1
                    curr1 = curr1.next
                else:
                    node.next = curr2
                    curr2 = curr2.next
            elif curr1:
                node.next = curr1
                curr1 = curr1.next
            elif curr2:
                node.next = curr2
                curr2 = curr2.next
            node = node.next
        return dummy.next

