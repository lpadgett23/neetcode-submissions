class MyHashSet:

    def __init__(self):
        self.hashdata = [False] * 1000001

    def add(self, key: int) -> None:
        #self.hashdata.insert(key, True) this would shift everything after it to the right, growing the list by 1
        self.hashdata[key] = True # this will replace the value at that index

    def remove(self, key: int) -> None:
        if self.hashdata[key]:
            self.hashdata[key] = False

    def contains(self, key: int) -> bool:
        return self.hashdata[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)