from pydantic import BaseModel, Field
from datetime import date
from typing import List, Optional

class TransactionRecord(BaseModel):
    date: str
    description: str
    amount: float
    category: str

class RiskMetrics(BaseModel):
    total_income: float = Field(..., description="Total inflows/earnings")
    total_spend: float = Field(..., description="Total outflows/expenses")
    net_savings: float = Field(..., description="Remaining cash flow")
    burn_rate_daily: float = Field(..., description="Average daily outflow")
    discretionary_spend_ratio: float = Field(
        ..., description="Percentage of spend on non-essentials"
    )

class AdvisoryPayload(BaseModel):
    metrics: RiskMetrics
    flagged_categories: List[str]
    suggested_action: str