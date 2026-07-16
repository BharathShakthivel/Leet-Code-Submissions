class Node: # Creating a node class and setting the initial next and prev pointers to None
    def __init__(self, key,val):
        self.key, self.val = key,val
        self.next = self.prev = None

class LRUCache:
    # Initialising the capacity and creating left and right dummy pointers
    # Creating a dict and naming it as cache to have faster lookup when dealing with get and put operations
    def __init__(self, capacity: int):
        self.cap = capacity
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        self.cache = {}
    
    def remove (self, node):
        prev,nxt = node.prev, node.next
        prev.next,nxt.prev = nxt,prev
    
    def insert (self, node):
        prev,nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev,nxt
    
    def get(self, key: int) -> int:
        if key in self.cache:
            #  before returning we must make the called element as least recently used.
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # Remove the least resently used node which is left most node.
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
