from quectosoft_hr.core.agent_loader import AgentLoader
from quectosoft_hr.orchestration.openclaw.templates import TemplateFactory
class OrchestratorAgent:
    def __init__(self):
        self.loader = AgentLoader()
        self.templates = TemplateFactory()
    async def health(self):
        return {'agent': 'orchestrator', 'status': 'healthy'}
    async def execute(self, payload, context=None):
        context = context or {}
        cards = self.loader.load_cards()
        project_hint = {
            'client_id': context.get('client_id', 'task-client'),
            'objective': payload.get('objective') or payload.get('request') or 'generic objective',
            'budget': payload.get('budget', 0),
            'timeline_days': payload.get('timeline_days', 0),
            'domain': context.get('domain', payload.get('domain', 'general')),
            'privacy_level': context.get('privacy_level', 'standard'),
        }
        plan = self.templates.build_plan(project_hint, cards)
        return {'orchestrated': True, 'dynamic_catalog_total': len(cards), 'matched_agent_cards': plan['matched_cards'], 'execution_preview': plan['execution_preview']}
