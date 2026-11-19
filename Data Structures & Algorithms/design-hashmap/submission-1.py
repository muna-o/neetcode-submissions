class MyHashMap:

    def __init__(self):
        self.num_buckets = 769
        self.buckets = [[] for _ in range(self.num_buckets)]

    def _hash(self, key):
        return key % self.num_buckets
        

    def put(self, key: int, value: int) -> None:
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        
        bucket.append([key, value])
        

    def get(self, key: int) -> int:
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        for k, v in bucket:
            if k == key:
                return v

        return -1
        

    def remove(self, key: int) -> None:
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)