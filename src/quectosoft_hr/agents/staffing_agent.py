from quectosoft_hr.core.base_agent import BaseAgent
from quectosoft_hr.core.models import AgentRole
from quectosoft_hr.core.serviceengine import ServiceEngine
from quectosoft_hr.tools.llm_tool import LLMTool
from quectosoft_hr.tools.memory_tool import MemoryTool
class StaffingAgent(BaseAgent):
    def __init__(self):
        super().__init__(AgentRole.STAFFING, 'staffing_agent')
        self.llm = LLMTool()
        self.memory = MemoryTool()
    async def execute(self, task):
        prompt = ServiceEngine.build_llm_instruction('staffing', task.payload, task.context)
        result = await self.llm.generate(prompt, system='You are a production-grade staffing specialist.')
        await self.memory.save('staffing:' + task.id, result)
        return {'service': 'staffing', 'service_context': ServiceEngine.build_service_context('staffing', task.payload, task.context), 'result': result}
