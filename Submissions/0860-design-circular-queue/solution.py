# class MyCircularQueue:

#     def __init__(self, k: int):
#         self.size = k
#         self.queue = []
#     def enQueue(self, value: int) -> bool:
#         if len(self.queue) >= self.size:
#             return False
#         self.queue.append(value)
#         return True

#     def deQueue(self) -> bool:
#         if not self.queue:
#             return False
#         self.queue.pop(0)
#         return True   

#     def Front(self) -> int:
#         if not self.queue:
#             return -1
#         return self.queue[0]

#     def Rear(self) -> int:
#         if not self.queue:
#             return -1
#         return self.queue[-1]

#     def isEmpty(self) -> bool:
#         if self.queue:
#             return False
#         return True
#     def isFull(self) -> bool:
#         if len(self.queue) == self.size:
#             return True
#         return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


# OPTIMISED VERSION
class ListNode:
    def __init__(self,val,next,prev):
        self.next = next
        self.val = val
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.left = ListNode(0,None,None)
        self.right = ListNode(0,None,self.left)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        cur = ListNode(value,self.right,self.right.prev) # BUGFIX - cur = ListNode(value,self.right,self.left)
        self.right.prev.next = cur
        self.right.prev = cur
        self.capacity-=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.capacity+=1
        return True

    def Front(self) -> int:
        if self.isEmpty():return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty():return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.capacity == 0
        
