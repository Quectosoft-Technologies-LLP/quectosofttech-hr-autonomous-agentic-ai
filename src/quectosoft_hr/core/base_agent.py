from abc import ABC, abstractmethod
from datetime import datetime
from quectosoft_hr.core.registry import AgentRegistry
from quectosoft_hr.core.eventbus import EVENT_BUS
from quectosoft_hr.core.models import TaskStatus
class BaseAgent(ABC):
    def __init__(self, role, name):
        self.role = role
        self.name = name
    def boot(self):
        AgentRegistry.register(self.name, self)
        EVENT_BUS.subscribe(self.role.value, self.on_task)
    async def on_task(self, task):
        task.status = TaskStatus.RUNNING
        task.updated_at = datetime.utcnow()
        try:
            task.result = await self.execute(task)
            task.status = TaskStatus.COMPLETED
        except Exception as exc:
            task.error = str(exc)
            task.status = TaskStatus.FAILED
    @abstractmethod
    async def execute(self, task):
        raise NotImplementedError
