import asyncio
from collections import defaultdict
class LiveEventHub:
    def __init__(self):
        self.subscribers = defaultdict(list)
        self._history = defaultdict(list)
    async def subscribe(self, stream_id):
        queue = asyncio.Queue()
        self.subscribers[stream_id].append(queue)
        for event in self._history.get(stream_id, []):
            await queue.put(event)
        return queue
    def unsubscribe(self, stream_id, queue):
        listeners = self.subscribers.get(stream_id, [])
        if queue in listeners:
            listeners.remove(queue)
    async def publish(self, stream_id, event):
        self._history[stream_id].append(event)
        for queue in list(self.subscribers.get(stream_id, [])):
            await queue.put(event)
    def history(self, stream_id):
        return list(self._history.get(stream_id, []))
GLOBAL_LIVE_HUB = LiveEventHub()
