import asyncio
from collections import defaultdict
class EventBus:
    def __init__(self):
        self.handlers = defaultdict(list)
        self.queue = asyncio.Queue()
        self.runner = None
    def subscribe(self, role, handler):
        self.handlers[role].append(handler)
    def emit(self, task):
        self.queue.put_nowait(task)
    async def dispatch(self):
        while True:
            task = await self.queue.get()
            for handler in self.handlers.get(task.role.value, []):
                await handler(task)
            self.queue.task_done()
    def start(self):
        if self.runner is None or self.runner.done():
            self.runner = asyncio.create_task(self.dispatch())
    async def shutdown(self):
        if self.runner:
            self.runner.cancel()
            try:
                await self.runner
            except asyncio.CancelledError:
                pass
EVENT_BUS = EventBus()
