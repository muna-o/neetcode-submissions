class MyHashMap:

    def __init__(self):
        self.BASE = 769
        self.data = [[] for _ in range(self.BASE)]

    def _hash(self, key: int) -> int:
        return key % self.BASE
        
    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        bucket = self.data[index]

        for i, (k, v) in enumerate(bucket):
            if key == k:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        

    def get(self, key: int) -> int:
        index = self._hash(key)
        bucket = self.data[index]

        for k, v in bucket:
            if key == k:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.data[index]

        for i, (k, v) in enumerate(bucket):
            if key == k:
                del bucket[i]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)