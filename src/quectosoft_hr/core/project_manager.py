from datetime import datetime
from uuid import uuid4
from quectosoft_hr.core.agent_loader import AgentLoader
from quectosoft_hr.core.live_events import GLOBAL_LIVE_HUB
from quectosoft_hr.core.model_router import ModelRouter
from quectosoft_hr.core.policy_enforcer import PolicyEnforcer
from quectosoft_hr.orchestration.openclaw.templates import TemplateFactory
from quectosoft_hr.raid.hitl_trigger import HITLTrigger
from quectosoft_hr.raid.mitigation_engine import MitigationEngine
from quectosoft_hr.raid.raid_entry import RAIDEntry
from quectosoft_hr.raid.raid_scorer import RAIDScorer
from quectosoft_hr.raid.raid_store import GLOBAL_RAID_STORE
from quectosoft_hr.raid.threshold_evaluator import ThresholdEvaluator

class ProjectManager:
    def __init__(self, catalog_root='config/agents/catalog'):
        self.projects = {}
        self.loader = AgentLoader(catalog_root)
        self.router = ModelRouter()
        self.policy = PolicyEnforcer()
        self.templates = TemplateFactory()
        self.scorer = RAIDScorer()
        self.thresholds = ThresholdEvaluator()
        self.mitigation = MitigationEngine()
        self.hitl = HITLTrigger()
    async def create_project(self, payload):
        project_id = str(uuid4())
        project = {
            'id': project_id,
            'client_id': payload.get('client_id', 'unknown'),
            'objective': payload.get('objective', ''),
            'budget': int(payload.get('budget', 0) or 0),
            'timeline_days': int(payload.get('timeline_days', 0) or 0),
            'domain': payload.get('domain', 'general'),
            'privacy_level': payload.get('privacy_level', 'standard'),
            'created_at': datetime.utcnow().isoformat(),
        }
        cards = self.loader.load_cards()
        project['recommended_provider'] = self.router.route(2, project['domain'].lower(), project['privacy_level'])
        project['policy_check'] = self.policy.validate({'raid_zone': 'medium', 'human_approved': True, 'public_data_dump': False})
        project['plan'] = self.templates.build_plan(project, cards)
        project['raid_entries'] = self._build_raid_entries(project)
        self.projects[project_id] = project
        await GLOBAL_LIVE_HUB.publish(project_id, {'type': 'project_created', 'project_id': project_id})
        await GLOBAL_LIVE_HUB.publish(project_id, {'type': 'plan_ready', 'project_id': project_id, 'nodes': len(project['plan']['nodes'])})
        return project
    def get_project(self, project_id):
        return self.projects.get(project_id)
    def list_catalog(self):
        cards = self.loader.load_cards()
        by_tier, by_department = {}, {}
        for card in cards:
            by_tier[str(card['tier'])] = by_tier.get(str(card['tier']), 0) + 1
            by_department[card['department']] = by_department.get(card['department'], 0) + 1
        return {'total_cards': len(cards), 'by_tier': by_tier, 'by_department': by_department}
    def _build_raid_entries(self, project):
        candidates = [('dependency', 'Cross-functional execution dependencies may slow delivery', 3, 3), ('assumption', 'Objective scope remains stable during planning', 2, 3)]
        if project['privacy_level'] == 'strict':
            candidates.append(('risk', 'Strict privacy scope increases approvals and review load', 4, 4))
        if project['domain'].lower() in {'bfsi', 'healthcare', 'govtech'}:
            candidates.append(('risk', f"{project['domain']} domain requires specialised validation", 4, 4))
        if project['budget'] >= 100000:
            candidates.append(('issue', 'Large budget requires stronger financial controls', 3, 5))
        items = []
        for category, description, likelihood, impact in candidates:
            entry = RAIDEntry(category=category, description=description, likelihood=likelihood, impact=impact, owner='system')
            score = self.scorer.score(entry)
            zone = self.thresholds.zone(score)
            record = {'category': category, 'description': description, 'score': score, 'zone': zone, 'mitigation': self.mitigation.recommend(zone), 'hitl': self.hitl.trigger(zone)}
            GLOBAL_RAID_STORE.add(record)
            items.append(record)
        return items
GLOBAL_PROJECT_MANAGER = ProjectManager()
