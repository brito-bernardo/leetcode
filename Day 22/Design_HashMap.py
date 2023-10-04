class MyHashMap:

    def __init__(self):
        self.size = 1000  # Choose a suitable size for the underlying array
        self.data = [None] * self.size

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        index = self._hash(key)
        if self.data[index] is None:
            self.data[index] = []
        for i, (k, v) in enumerate(self.data[index]):
            if k == key:
                self.data[index][i] = (key, value)
                return
        self.data[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        if self.data[index] is not None:
            for k, v in self.data[index]:
                if k == key:
                    return v
        return -1

    def remove(self, key):
        index = self._hash(key)
        if self.data[index] is not None:
            for i, (k, v) in enumerate(self.data[index]):
                if k == key:
                    del self.data[index][i]
                    return

