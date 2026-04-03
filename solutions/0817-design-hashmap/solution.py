class MyHashMap:
    def __init__(self):
        # Using 1000 buckets for efficient distribution
        self.size = 1000
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hash_key = self._hash(key)
        for pair in self.table[hash_key]:
            if pair[0] == key:
                pair[1] = value  # Update existing key
                return
        self.table[hash_key].append([key, value])  # Add new pair

    def get(self, key: int) -> int:
        hash_key = self._hash(key)
        for pair in self.table[hash_key]:
            if pair[0] == key:
                return pair[1]
        return -1  # Key not found

    def remove(self, key: int) -> None:
        hash_key = self._hash(key)
        for i, pair in enumerate(self.table[hash_key]):
            if pair[0] == key:
                self.table[hash_key].pop(i)
                return

