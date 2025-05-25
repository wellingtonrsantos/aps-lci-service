from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models.lci_models import LCIFlow, LCIProduct
from app.db.database import get_session


router = APIRouter()


@router.get("/products")
async def list_products(session: Session = Depends(get_session)):
    result = session.exec(select(LCIProduct)).all()
    return [{"id": p.id, "name": p.name, "description": p.description} for p in result]


@router.get("/products/{product_id}")
async def get_lci_by_product_id(
    product_id: int, session: Session = Depends(get_session)
):
    statement = select(LCIFlow).where(LCIFlow.product_id == product_id)
    flows = session.exec(statement).all()

    if not flows:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    return [
        {
            "Flow Name": f.flow_name,
            "Amount": f.amount,
            "Unit": f.unit,
            "Flow Direction": f.flow_direction,
            "UEV": f.uev,
            "Category": f.category,
        }
        for f in flows
    ]
