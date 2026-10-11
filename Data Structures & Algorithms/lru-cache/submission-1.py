class LRUCache:

    def __init__(self, capacity: int):
        self.i = 0
        self.capacity = capacity
        self.data = {}
        self.last_accessed = {}
        

    def get(self, key: int) -> int:
        if key in self.data:
            self.last_accessed[key] = self.i
            self.i += 1
            return self.data[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data[key] = value
            self.last_accessed[key] = self.i
            self.i += 1
        else:
            self.data[key] = value
            self.last_accessed[key] = self.i
            self.i += 1

        if len(self.data) > self.capacity:
            min_i = None
            min_key = None

            for (key, value) in self.last_accessed.items():
                if min_i == None or min_i > self.last_accessed[key]:
                    min_i = self.last_accessed[key]
                    min_key = key

            self.last_accessed.pop(min_key)
            self.data.pop(min_key)

        
