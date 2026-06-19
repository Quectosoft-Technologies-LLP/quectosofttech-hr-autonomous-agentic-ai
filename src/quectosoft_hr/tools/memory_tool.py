class MemoryTool:
    def __init__(self):
        self.store = {}
    async def save(self, key, data):
        self.store[key] = data
    async def recall(self, key):
        return self.store.get(key)
