from dataclasses import dataclass, field
from typing import Any
@dataclass
class DAGNode:
    node_id: str
    role: str
    payload: dict[str, Any] = field(default_factory=dict)
    dependencies: list[str] = field(default_factory=list)
class DAG:
    def __init__(self):
        self.nodes = {}
    def add_node(self, node):
        self.nodes[node.node_id] = node
    def ready_nodes(self, completed):
        return [n for n in self.nodes.values() if n.node_id not in completed and all(dep in completed for dep in n.dependencies)]
