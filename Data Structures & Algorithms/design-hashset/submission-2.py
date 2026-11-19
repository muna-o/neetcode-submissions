class MyHashSet:

    def __init__(self):
        self.num_buckets = 769
        self.buckets = [[] for _ in range(self.num_buckets)]  

    def _hash(self, key):
        return key % self.num_buckets      

    def add(self, key: int) -> None:
        bucket_index = self.buckets[self._hash(key)]
        if key not in bucket_index:
            bucket_index.append(key)
        

    def remove(self, key: int) -> None:
        bucket_index = self.buckets[self._hash(key)]
        if key in bucket_index:
            bucket_index.remove(key)
        

    def contains(self, key: int) -> bool:
        bucket_index = self.buckets[self._hash(key)]
        return key in bucket_index
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)