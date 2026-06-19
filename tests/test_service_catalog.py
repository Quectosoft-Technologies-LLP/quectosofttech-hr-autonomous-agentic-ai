from quectosoft_hr.core.servicecatalog import SERVICE_CATALOG, get_service_definition
def test_catalog_contains_enterprise_services():
    for key in ["staffing", "payroll", "posh", "compliance", "policy", "hrms", "audit", "learning", "insurance"]:
        assert key in SERVICE_CATALOG
def test_compliance_and_policy_are_complete():
    assert "PF compliance" in get_service_definition("compliance").services
    assert "Employee handbook" in get_service_definition("policy").services
