# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # We use fast pointer and slow pointer technique to reach half way point
        # The slow pointer next element would be the half way through point.
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = prev= None
        # Upon reaching the half way point, the slow pointer;s next element would be the second half
        # So we will break the link and set it to null
        # We will reverse the remaining elements through reversing the econd half of the linked list.
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        # Prev would be the head of the newly reversed second half of the linked list
        
        #  At last we merge the list as required in the problem
        first,second = head,prev 
        while second:
            tmp1,tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1,tmp2



        

