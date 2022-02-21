from app.crud.crud_base import CRUDBase
from app.models.plan import Plan
from app.schemas import PlanCreate, PlanUpdate


class CRUDPlan(CRUDBase[Plan, PlanCreate, PlanUpdate]):
    pass


plan = CRUDPlan(Plan)
