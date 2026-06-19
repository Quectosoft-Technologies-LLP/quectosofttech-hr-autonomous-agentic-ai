from dataclasses import dataclass
@dataclass
class ServiceDefinition:
    name: str
    benefits: list[str]
    services: list[str]
SERVICE_CATALOG = {
    "staffing": ServiceDefinition("Staffing", ["faster hiring"], ["recruitment", "screening"]),
    "payroll": ServiceDefinition("Payroll", ["accurate lifecycle ops"], ["payroll processing"]),
    "posh": ServiceDefinition("PoSH", ["safer workplace"], ["policy handling"]),
    "compliance": ServiceDefinition("Compliance", ["regulatory alignment"], ["PF compliance", "labour law"]),
    "policy": ServiceDefinition("Policy", ["governed operations"], ["Employee handbook", "SOP drafting"]),
    "hrms": ServiceDefinition("HRMS", ["systemized operations"], ["implementation support"]),
    "learning": ServiceDefinition("Learning", ["capability uplift"], ["curriculum planning"]),
    "audit": ServiceDefinition("Audit", ["traceability"], ["governance review"]),
    "insurance": ServiceDefinition("Insurance", ["risk cover"], ["benefits review"]),
}
def get_service_definition(name):
    return SERVICE_CATALOG[name]
