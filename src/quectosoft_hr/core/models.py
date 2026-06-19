from enum import Enum
from datetime import datetime
from typing import Any
from uuid import uuid4
from pydantic import BaseModel, Field

class AgentRole(str, Enum):
    STAFFING = 'staffing'
    PAYROLL = 'payroll'
    POSH = 'posh'
    COMPLIANCE = 'compliance'
    POLICY = 'policy'
    HRMS = 'hrms'
    LEARNING = 'learning'
    AUDIT = 'audit'
    INSURANCE = 'insurance'
    ORCHESTRATOR = 'orchestrator'

class TaskPriority(int, Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class TaskStatus(str, Enum):
    PENDING = 'pending'
    RUNNING = 'running'
    COMPLETED = 'completed'
    FAILED = 'failed'
    ESCALATED = 'escalated'

class HRTask(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    role: AgentRole
    priority: TaskPriority = TaskPriority.MEDIUM
    status: TaskStatus = TaskStatus.PENDING
    payload: dict[str, Any] = Field(default_factory=dict)
    context: dict[str, Any] = Field(default_factory=dict)
    result: dict[str, Any] | None = None
    error: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    assigned_agent: str | None = None
