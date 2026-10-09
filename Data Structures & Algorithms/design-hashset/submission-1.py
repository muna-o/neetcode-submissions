class MyHashSet:

    def __init__(self):
        self.BASE = 769
        self.data = [[] for _ in range(self.BASE)]  

    def _hash(self, key: int):
        return key % self.BASE
        

    def add(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.data[index]

        if key not in bucket:
            bucket.append(key)
        
        

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.data[index]

        if key in bucket:
            bucket.remove(key)
        
        

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        bucket = self.data[index]

        return key in bucket
        

        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)