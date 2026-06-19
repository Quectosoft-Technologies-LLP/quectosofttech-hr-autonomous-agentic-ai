from quectosoft_hr.orchestration.openclaw.approval_engine import ApprovalEngine
from quectosoft_hr.orchestration.openclaw.hitl_manager import HITLManager
class DAGRunner:
    def __init__(self):
        self.approval = ApprovalEngine()
        self.hitl = HITLManager()
    def run(self, dag, risk_zones=None):
        completed, execution_order, approvals = set(), [], []
        risk_zones = risk_zones or {}
        while len(completed) < len(dag.nodes):
            ready = [n for n in dag.ready_nodes(completed) if n.node_id not in completed]
            if not ready:
                raise ValueError("DAG deadlock detected")
            for node in ready:
                zone = risk_zones.get(node.node_id, "low")
                if self.hitl.should_pause(zone):
                    approvals.append({"node_id": node.node_id, "zone": zone, "approver": self.approval.required_approver(zone), "channel": self.hitl.channel(zone)})
                completed.add(node.node_id)
                execution_order.append(node.node_id)
        return {"execution_order": execution_order, "approvals": approvals}
