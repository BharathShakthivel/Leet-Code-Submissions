# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]: 
        dummy = ListNode(0,head)
        Left_prev, cur = dummy,head

        # 1st Phase -Shifting the current till it reaches left index to place the Left_Prev before current
        #  It is gonna be LEft -1 times
        for i in range(left-1):
            Left_prev, cur = cur, cur.next


        # 2nd Phase - Shifting the current till it reaches right pointer + 1
        #  In between we are reversing all
        prev = None
        for j in range(right-left+1):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        

        # Initial Left pointer's next element should point to the element after the the right index which is the
        # current element i.e,cur
        #  Initial left pointer should point to the right index element i.e, prev
        Left_prev.next.next = cur
        Left_prev.next = prev
        return dummy.next
