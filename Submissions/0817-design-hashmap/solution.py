class MyHashMap:

    def __init__(self):
        self.my_list ={}

    def put(self, key: int, value: int) -> None:
        if key in self.my_list:
          self.my_list.update({key:value})
        else:
          self.my_list[key] = value

    def get(self, key: int) -> int:
        if key in self.my_list:
            return self.my_list.get(key)
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.my_list:
            self.my_list.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
