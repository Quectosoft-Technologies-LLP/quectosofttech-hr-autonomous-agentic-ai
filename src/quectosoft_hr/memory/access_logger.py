class MemoryAccessLogger:
    def __init__(self):
        self.events = []
    def log(self, actor, scope, action):
        self.events.append({"actor": actor, "scope": scope, "action": action})
