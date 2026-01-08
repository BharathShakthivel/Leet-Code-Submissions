class MyHashSet:

    def __init__(self):
        self.my_set = []
    def add(self, key: int) -> None:
                if key not in self.my_set:
                    self.my_set.append(key)
                    return self.my_set
                else:
                    pass
    def remove(self, key: int) -> None:
                if key in self.my_set:
                    self.my_set.remove(key)        
                    return self.my_set
                else:
                    pass
    def contains(self, key: int) -> bool:
                if key in self.my_set:
                    return True
                else:
                    return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
