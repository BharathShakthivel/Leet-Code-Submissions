# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Two pointer technique - Big O n Notation
        prev, curr = None,head
        # We assign previous pointer as Null and Current Pointer as head
        while curr:
            # We loop through the linked lIst from Head until it reaches and end
            nxt = curr.next
            # WE assign the pointer to next element of the linked list to nxt variable
            curr.next = prev
            # We break the link and point to the previous element of the linked list.
            prev = curr
            #The previous pointer is shifted and made as the current pointer.
            curr = nxt
            # The current pointer is shifted and pointing to the next element of the linked list with the help of the variable nxt which was stored initially.
        return prev
            # When the loop breaks the prev pointer would point to the head of the element after reversing the Linked list, so we simply return the head.
