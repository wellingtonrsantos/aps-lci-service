from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional


class LCIProduct(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None

    flows: List["LCIFlow"] = Relationship(back_populates="product")


class LCIFlow(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="lciproduct.id")

    flow_name: str
    amount: float
    unit: str
    flow_direction: str
    uev: float
    category: str

    product: LCIProduct = Relationship(back_populates="flows")
