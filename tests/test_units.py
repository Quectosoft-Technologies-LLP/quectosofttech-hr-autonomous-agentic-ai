from quectosoft_hr.units.corporate.legal import LegalUnit
from quectosoft_hr.units.corporate.finance import FinanceUnit
from quectosoft_hr.units.corporate.admin import AdminUnit
from quectosoft_hr.units.corporate.security import SecurityUnit
from quectosoft_hr.units.corporate.infra import InfraUnit
from quectosoft_hr.units.presales.presales import PresalesUnit
from quectosoft_hr.units.presales.sales import SalesUnit
from quectosoft_hr.units.presales.proposal import ProposalUnit
from quectosoft_hr.units.domains.telecom import TelecomUnit
from quectosoft_hr.units.domains.healthcare import HealthcareUnit
from quectosoft_hr.units.domains.retail import RetailUnit
from quectosoft_hr.units.domains.manufacturing import ManufacturingUnit
from quectosoft_hr.units.domains.govtech import GovtechUnit
def test_corporate_units_route():
    assert LegalUnit().route("contract review")["routed"] is True
    assert FinanceUnit().route("budget control")["routed"] is True
    assert AdminUnit().route("facility support")["routed"] is True
    assert SecurityUnit().route("incident triage")["routed"] is True
    assert InfraUnit().route("cluster scaling")["routed"] is True
def test_presales_units_route():
    assert PresalesUnit().route("qualify lead")["qualified"] is True
    assert SalesUnit().route("advance deal")["engaged"] is True
    assert ProposalUnit().route("draft proposal")["drafted"] is True
def test_domain_units_review():
    assert TelecomUnit().review("telco objective")["reviewed"] is True
    assert HealthcareUnit().review("care workflow")["reviewed"] is True
    assert RetailUnit().review("store rollout")["reviewed"] is True
    assert ManufacturingUnit().review("plant process")["reviewed"] is True
    assert GovtechUnit().review("citizen portal")["reviewed"] is True
