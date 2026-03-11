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
        # Two Pass Algorithm
        old_copy = {None:None} # To handle edge case of current pointer pointing to NULL when traversing.
        cur = head
        while cur:
            old_copy[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            copy = old_copy[cur]
            copy.next = old_copy[cur.next]
            copy.random = old_copy[cur.random]
            cur=cur.next
        return old_copy[head]
