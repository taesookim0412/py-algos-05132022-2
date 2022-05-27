class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key) -> int:
        for kv in self.bucket:
            if kv[0] == key:
                return kv[1]
        return -1

    def update(self, key, value):
        for kv in self.bucket:
            if kv[0] == key:
                kv[1] = value
                return
        self.bucket.append([key, value])

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                del self.bucket[i]


class MyHashMap:
    hashLen = 2069

    def __init__(self):
        self.hashMap = [Bucket() for _ in range(self.hashLen)]

    def put(self, key: int, value: int) -> None:
        hashKey = key % self.hashLen
        self.hashMap[hashKey].update(key, value)

    def get(self, key: int) -> int:
        if key < 0:
            return -1
        hashKey = key % self.hashLen
        return self.hashMap[hashKey].get(key)

    def remove(self, key: int) -> None:
        hashKey = key % self.hashLen
        self.hashMap[hashKey].remove(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)