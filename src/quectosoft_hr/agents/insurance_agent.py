from quectosoft_hr.core.base_agent import BaseAgent
from quectosoft_hr.core.models import AgentRole
from quectosoft_hr.core.serviceengine import ServiceEngine
from quectosoft_hr.tools.llm_tool import LLMTool
from quectosoft_hr.tools.memory_tool import MemoryTool
class InsuranceAgent(BaseAgent):
    def __init__(self):
        super().__init__(AgentRole.INSURANCE, 'insurance_agent')
        self.llm = LLMTool()
        self.memory = MemoryTool()
    async def execute(self, task):
        prompt = ServiceEngine.build_llm_instruction('insurance', task.payload, task.context)
        result = await self.llm.generate(prompt, system='You are a production-grade insurance specialist.')
        await self.memory.save('insurance:' + task.id, result)
        return {'service': 'insurance', 'service_context': ServiceEngine.build_service_context('insurance', task.payload, task.context), 'result': result}
