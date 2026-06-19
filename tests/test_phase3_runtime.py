import asyncio
from quectosoft_hr.core.agent_loader import AgentLoader
from quectosoft_hr.core.model_router import ModelRouter
from quectosoft_hr.orchestration.openclaw.templates import TemplateFactory
from quectosoft_hr.core.project_manager import ProjectManager
from quectosoft_hr.raid.threshold_evaluator import ThresholdEvaluator
def test_catalog_loads_expanded_cards():
    assert len(AgentLoader().load_cards()) >= 70
def test_model_router_prefers_private_local_for_strict():
    assert ModelRouter().route(2, privacy_level="strict") == "ollama"
def test_openclaw_template_adds_domain_and_finance_nodes():
    plan = TemplateFactory().build_plan({"client_id": "acme", "objective": "Build BFSI portal", "budget": 120000, "timeline_days": 30, "domain": "bfsi", "privacy_level": "strict"}, AgentLoader().load_cards())
    node_ids = {node["node_id"] for node in plan["nodes"]}
    assert "bfsi_domain_review" in node_ids
    assert "finance_review" in node_ids
    assert plan["execution_preview"]["approvals"]
def test_threshold_evaluator():
    t = ThresholdEvaluator()
    assert t.zone(4) == "low"
    assert t.zone(10) == "medium"
    assert t.zone(16) == "high"
    assert t.zone(25) == "critical"
def test_project_manager_creates_project_with_raid():
    project = asyncio.run(ProjectManager().create_project({"client_id": "acme", "objective": "Launch healthcare onboarding platform", "budget": 50000, "timeline_days": 45, "domain": "healthcare", "privacy_level": "strict"}))
    assert project["recommended_provider"] == "ollama"
    assert project["plan"]["matched_cards"]
    assert project["raid_entries"]
