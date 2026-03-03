# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        current = ans
        carry = 0
        while l1 or l2 or carry!=0:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0
            total = val_1 + val_2 + carry
            new_digit = total % 10
            carry = (total // 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            current.next =  ListNode(new_digit)
            current = current.next
        return ans.next


