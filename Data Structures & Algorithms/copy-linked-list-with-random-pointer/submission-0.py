"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        old_to_new = {None : None}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            copy_node = old_to_new[curr]
            copy_node.next = old_to_new[curr.next]
            copy_node.random = old_to_new[curr.random]
            curr = curr.next
        return old_to_new[head]
