from quectosoft_hr.orchestration.openclaw.dag import DAG, DAGNode
from quectosoft_hr.orchestration.openclaw.dag_runner import DAGRunner
class TemplateFactory:
    def __init__(self):
        self.runner = DAGRunner()
    def build_project_dag(self, project, agent_cards):
        domain = project.get('domain', 'general').lower()
        dag = DAG()
        dag.add_node(DAGNode('board_review', 'board', {'objective': project.get('objective')}))
        dag.add_node(DAGNode('executive_planning', 'csuite', {'client_id': project.get('client_id')}, ['board_review']))
        dag.add_node(DAGNode('requirements', 'requirements', {'objective': project.get('objective')}, ['executive_planning']))
        dag.add_node(DAGNode('policy_review', 'policy', {'privacy_level': project.get('privacy_level')}, ['requirements']))
        dag.add_node(DAGNode('compliance_review', 'compliance', {'domain': domain}, ['policy_review']))
        dag.add_node(DAGNode('staffing_plan', 'staffing', {'timeline_days': project.get('timeline_days')}, ['executive_planning']))
        dag.add_node(DAGNode('engineering', 'engineering', {'domain': domain}, ['requirements', 'compliance_review']))
        dag.add_node(DAGNode('qa', 'qa', {}, ['engineering']))
        dag.add_node(DAGNode('devops', 'devops', {}, ['qa']))
        if domain in {'bfsi', 'telecom', 'healthcare', 'retail', 'manufacturing', 'govtech'}:
            dag.add_node(DAGNode(f'{domain}_domain_review', 'domain_control', {'domain': domain}, ['compliance_review']))
        if int(project.get('budget', 0) or 0) >= 100000:
            dag.add_node(DAGNode('finance_review', 'finance', {'budget': project.get('budget')}, ['executive_planning']))
        return dag
    def risk_zones(self, project):
        zones = {'board_review': 'medium', 'executive_planning': 'medium'}
        if project.get('privacy_level') == 'strict':
            zones['policy_review'] = 'high'
            zones['compliance_review'] = 'high'
        if project.get('domain', '').lower() in {'bfsi', 'healthcare', 'govtech'}:
            zones[f"{project.get('domain').lower()}_domain_review"] = 'high'
        if int(project.get('budget', 0) or 0) >= 100000:
            zones['finance_review'] = 'high'
        return zones
    def match_cards(self, project, agent_cards):
        objective = project.get('objective', '').lower()
        domain = project.get('domain', '').lower()
        matches = []
        for card in agent_cards:
            text = ' '.join([str(card.get('department', '')), str(card.get('role', '')), str(card.get('name', '')), ' '.join(card.get('responsibilities', []))]).lower()
            if domain and domain in text:
                matches.append({'id': card['id'], 'name': card['name'], 'tier': card['tier'], 'department': card['department']})
                continue
            if any(token and token in text for token in objective.split()[:6]):
                matches.append({'id': card['id'], 'name': card['name'], 'tier': card['tier'], 'department': card['department']})
        dedup, seen = [], set()
        for item in matches:
            if item['id'] not in seen:
                seen.add(item['id'])
                dedup.append(item)
        return dedup[:20]
    def build_plan(self, project, agent_cards):
        dag = self.build_project_dag(project, agent_cards)
        return {'nodes': [{'node_id': n.node_id, 'role': n.role, 'dependencies': n.dependencies} for n in dag.nodes.values()], 'execution_preview': self.runner.run(dag, self.risk_zones(project)), 'matched_cards': self.match_cards(project, agent_cards)}
