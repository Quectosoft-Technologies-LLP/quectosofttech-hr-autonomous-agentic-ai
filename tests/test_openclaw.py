from quectosoft_hr.orchestration.openclaw.dag import DAG, DAGNode
from quectosoft_hr.orchestration.openclaw.dag_runner import DAGRunner
def test_openclaw_runner_orders_dependencies():
    dag = DAG()
    dag.add_node(DAGNode("a", "requirements"))
    dag.add_node(DAGNode("b", "engineering", dependencies=["a"]))
    dag.add_node(DAGNode("c", "qa", dependencies=["b"]))
    result = DAGRunner().run(dag, {"c": "high"})
    assert result["execution_order"] == ["a", "b", "c"]
    assert result["approvals"][0]["approver"] == "csuite"
