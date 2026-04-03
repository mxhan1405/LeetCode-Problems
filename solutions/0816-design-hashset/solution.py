class MyHashSet:
    def __init__(self):
        # Choose a prime number for the number of buckets to reduce collisions
        self.num_buckets = 1000
        self.buckets = [[] for _ in range(self.num_buckets)]

    def _hash(self, key: int) -> int:
        # Simple modulo hash function
        return key % self.num_buckets

    def add(self, key: int) -> None:
        hash_index = self._hash(key)
        if key not in self.buckets[hash_index]:
            self.buckets[hash_index].append(key)

    def remove(self, key: int) -> None:
        hash_index = self._hash(key)
        if key in self.buckets[hash_index]:
            self.buckets[hash_index].remove(key)

    def contains(self, key: int) -> bool:
        hash_index = self._hash(key)
        return key in self.buckets[hash_index]

